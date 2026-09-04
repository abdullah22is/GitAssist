"""GitHub/Git remote URL parsing and information extraction."""

import re
import json
import urllib.request
import urllib.error
import webbrowser
from gitassist.git import repository
from gitassist.cli import output
from gitassist.localization.texts import get_text


def parse_remote_url(url: str):
    if not url:
        return None, None, None

    https_match = re.match(r"https?://([^/]+)/([^/]+)/([^/]+?)(?:\.git)?/?$", url)
    if https_match:
        host = https_match.group(1)
        owner = https_match.group(2)
        repo = https_match.group(3)
        provider = "github" if "github" in host else ("gitlab" if "gitlab" in host else ("bitbucket" if "bitbucket" in host else host))
        return provider, owner, repo

    ssh_match = re.match(r"git@([^:]+):([^/]+)/([^/]+?)(?:\.git)?$", url)
    if ssh_match:
        host = ssh_match.group(1)
        owner = ssh_match.group(2)
        repo = ssh_match.group(3)
        provider = "github" if "github" in host else ("gitlab" if "gitlab" in host else ("bitbucket" if "bitbucket" in host else host))
        return provider, owner, repo

    return None, None, None


def show_remote_details():
    url = repository.get_remote_info()
    if not url:
        output.print_warning("remote_not_configured")
        return

    provider, owner, repo = parse_remote_url(url)
    output.print_info(get_text("remote_url", url=url))
    if provider:
        output.print_info(get_text("provider", provider=provider))
    if owner:
        output.print_info(get_text("owner", owner=owner))
    if repo:
        output.print_info(get_text("repo_name", repo=repo))


def open_repo_in_browser():
    url = repository.get_remote_info()
    if not url:
        output.print_warning("remote_not_configured")
        return

    if url.startswith("git@"):
        url = re.sub(r"git@([^:]+):", r"https://\1/", url)
    if url.endswith(".git"):
        url = url[:-4]

    output.print_info(get_text("opening_url", url=url))
    try:
        webbrowser.open(url)
        output.print_success("browser_opened")
    except Exception as e:
        output.print_error("browser_open_failed", error=str(e))


def create_github_repo(token, repo_name, private=False, description=""):
    url = "https://api.github.com/user/repos"
    data = json.dumps({
        "name": repo_name,
        "private": private,
        "description": description,
    }).encode("utf-8")

    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Authorization", f"token {token}")
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "GitAssist")

    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 201:
                result = json.loads(response.read().decode("utf-8"))
                return result.get("clone_url")
            else:
                return None
    except urllib.error.HTTPError:
        return None
    except Exception:
        return None