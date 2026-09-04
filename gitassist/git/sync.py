"""Git synchronization operations (fetch, pull, push)."""

from gitassist.git.executor import run_git_command
from gitassist.git import repository
from gitassist.cli import output


def fetch(remote="origin"):
    """Fetch changes from remote without merging."""
    return run_git_command(["git", "fetch", remote], f"Fetching from {remote}...")


def pull(remote="origin", branch=None):
    """Pull changes from remote and merge into current branch."""
    cmd = ["git", "pull"]
    if remote:
        cmd.append(remote)
    if branch:
        cmd.append(branch)
    return run_git_command(cmd, "Pulling changes from remote...")


def push(remote="origin", branch=None):
    """Push local commits to remote."""
    cmd = ["git", "push"]
    if remote:
        cmd.append(remote)
    if branch:
        cmd.append(branch)
    return run_git_command(cmd, "Pushing changes to remote...")


def has_remote_updates(remote="origin"):
    """
    Check if there are remote updates available.
    Returns True if local branch is behind remote, False otherwise.
    """
    if not repository.has_remote():
        return False

    # Fetch first to get latest remote info
    if not fetch(remote):
        return False

    # Compare local and remote
    branch = repository.get_current_branch()
    if not branch:
        return False

    result = run_git_command(["git", "rev-list", "--count", f"HEAD..{remote}/{branch}"],
                             "", show_output=False, interactive=False)
    if result is False:
        return False

    # We need to capture output from run_git_command, but it only returns bool.
    # Instead, we'll do a direct subprocess here.
    import subprocess
    try:
        res = subprocess.run(
            ["git", "rev-list", "--count", f"HEAD..{remote}/{branch}"],
            capture_output=True, text=True, check=False
        )
        if res.returncode == 0 and res.stdout.strip().isdigit():
            count = int(res.stdout.strip())
            return count > 0
    except Exception:
        pass
    return False