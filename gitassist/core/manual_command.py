"""Manual command entry mode with typo detection and AI/rule-based support."""

import difflib
from gitassist.cli.output import print_info, print_warning, print_error, print_title
from gitassist.cli.input_handler import ask_input, ask_yes_no
from gitassist.git.executor import run_git_command
from gitassist.localization.texts import get_text
from gitassist.config import settings
from gitassist.ai.intent import interpret_user_input
from gitassist.git.repository import get_repo_state_summary

COMMON_COMMANDS = [
    "status", "init", "add", "commit", "log", "branch", "checkout",
    "switch", "merge", "stash", "pull", "push", "fetch", "clone", "remote"
]


def suggest_correction(user_cmd):
    """Suggest a correction for a mistyped Git subcommand."""
    if not user_cmd.startswith("git "):
        return None
    parts = user_cmd.split()
    if len(parts) < 2:
        return None
    subcmd = parts[1]
    closest = difflib.get_close_matches(subcmd, COMMON_COMMANDS, n=1, cutoff=0.7)
    if closest and closest[0] != subcmd:
        return user_cmd.replace(subcmd, closest[0], 1)
    return None


def execute_text_command(command_str):
    """Process a text command directly (from voice or other input)."""
    if not command_str.startswith("git "):
        print_info(get_text("interpreting"))
        suggestion = interpret_user_input(command_str, get_repo_state_summary())
        if suggestion:
            print_info(get_text("ai_suggestion", command=suggestion))
            if ask_yes_no(get_text("execute_suggested")):
                command_str = suggestion
            else:
                return
        else:
            print_error(get_text("invalid_command"))
            return

    suggested = suggest_correction(command_str)
    if suggested:
        print_warning(get_text("typo_detected"))
        print_info(get_text("you_entered", command=command_str))
        print_info(get_text("did_you_mean", suggestion=suggested))
        if ask_yes_no(get_text("execute_corrected")):
            command_str = suggested

    parts = command_str.split()
    command_list = parts if parts[0] == "git" else ["git"] + parts
    run_git_command(command_list, get_text("executing_manual"))


def manual_command_mode():
    """Handle manual Git command entry."""
    print_title(get_text("manual_mode_title"))
    command_str = ask_input(get_text("enter_git_command"), allow_empty=False)
    execute_text_command(command_str)