"""Controlled execution of Git commands."""

import subprocess
from gitassist.cli.output import print_info, print_warning, print_error
from gitassist.cli.input_handler import ask_yes_no
from gitassist.security.analyzer import analyze_command
from gitassist.security.risk import risk_to_string, RiskLevel
from gitassist.errors.analyzer import analyze_error
from gitassist.security.context import check_context
from gitassist.config import settings
from gitassist.logging.logger import logger
from gitassist.localization.texts import get_text


def run_git_command(
    command: list[str],
    description: str = "",
    show_output: bool = True,
    interactive: bool = True,
    lang: str = None,
) -> bool:
    """
    Execute a Git command safely using a list of arguments.
    """
    if lang is None:
        lang = settings.LANGUAGE

    if settings.DRY_RUN:
        print_info(get_text("dry_run_message", lang, command=' '.join(command)))
        logger.info(f"Dry-run: would execute: {' '.join(command)}")
        return True

    if description:
        print_info(description)

    is_appropriate, context_warning, context_alternative = check_context(command)
    if not is_appropriate:
        print_warning(context_warning)
        if context_alternative:
            print_info(context_alternative)
        if interactive:
            if not ask_yes_no(get_text("confirm_continue", lang)):
                print_info(get_text("command_cancelled", lang))
                logger.info(f"Command cancelled by user: {' '.join(command)}")
                return False

    risk_level, warning, alternative = analyze_command(command)

    if risk_level != RiskLevel.SAFE:
        print_warning(get_text("risk_level", lang, level=risk_to_string(risk_level)))
        if warning:
            print_warning(warning)
        if alternative:
            print_info(get_text("safer_alternative", lang, alternative=alternative))

        if interactive:
            if not ask_yes_no(get_text("confirm_continue", lang)):
                print_info(get_text("command_cancelled", lang))
                logger.info(f"Command cancelled by user: {' '.join(command)}")
                return False

    logger.info(f"Executing command: {' '.join(command)}")
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode == 0:
            if show_output and result.stdout:
                print(result.stdout)
            logger.info(f"Command succeeded: {' '.join(command)}")
            return True
        else:
            print_error(get_text("command_failed", lang, command=' '.join(command)))
            if result.stderr:
                print(result.stderr)
            explanation = analyze_error(result.stderr)
            if explanation:
                print_info(explanation)
            logger.error(f"Command failed: {' '.join(command)} - {result.stderr}")
            return False
    except Exception as exc:
        print_error(get_text("unexpected_error", lang, error=str(exc)))
        logger.error(f"Exception while executing {' '.join(command)}: {exc}")
        return False