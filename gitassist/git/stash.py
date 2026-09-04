"""Git stash operations."""

from gitassist.git.executor import run_git_command


def save_stash(message=""):
    """Save current changes to stash."""
    cmd = ["git", "stash", "push"]
    if message:
        cmd.extend(["-m", message])
    return run_git_command(cmd, "Saving changes to stash...")


def list_stashes():
    """List all stashes."""
    return run_git_command(["git", "stash", "list"], "Listing stashes...")


def pop_stash():
    """Apply and remove the most recent stash."""
    return run_git_command(["git", "stash", "pop"], "Applying and removing latest stash...")


def apply_stash():
    """Apply the most recent stash without removing it."""
    return run_git_command(["git", "stash", "apply"], "Applying latest stash...")


def drop_stash():
    """Drop the most recent stash."""
    return run_git_command(["git", "stash", "drop"], "Dropping latest stash...")