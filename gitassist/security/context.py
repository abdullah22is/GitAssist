"""Context-aware command checking."""

from gitassist.git import repository
from gitassist.localization.texts import get_text


def check_context(command_list):
    """Return (is_appropriate, warning_text, alternative_text)."""
    if not repository.is_git_repo():
        if command_list[0] == "git" and command_list[1] in ("init", "clone"):
            return True, "", ""
        else:
            return False, get_text("warning_not_git_repo"), get_text("suggestion_init_or_clone")

    command = " ".join(command_list)

    if command.startswith("git merge") or command.startswith("git pull"):
        if repository.has_uncommitted_changes():
            return False, get_text("warning_uncommitted_changes"), get_text("suggestion_commit_or_stash")

    if command.startswith("git push"):
        if not repository.get_remote_info():
            return False, get_text("warning_no_remote"), get_text("suggestion_add_remote")

    return True, "", ""