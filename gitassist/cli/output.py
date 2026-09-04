"""Output formatting utilities for the CLI."""

from gitassist.localization.texts import get_text
from gitassist.config import settings

class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"


def print_banner():
    print(f"{Colors.CYAN}{Colors.BOLD}================================{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}        GitAssist v0.1.0        {Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}   Smart & Safe Git Assistant   {Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}================================{Colors.RESET}")


def print_info(message, lang=None, **kwargs):
    if lang is None:
        lang = settings.LANGUAGE
    text = get_text(message, lang, **kwargs)
    print(f"{Colors.CYAN}[INFO]{Colors.RESET} {text}")


def print_success(message, lang=None, **kwargs):
    if lang is None:
        lang = settings.LANGUAGE
    text = get_text(message, lang, **kwargs)
    print(f"{Colors.GREEN}[SUCCESS]{Colors.RESET} {text}")


def print_warning(message, lang=None, **kwargs):
    if lang is None:
        lang = settings.LANGUAGE
    text = get_text(message, lang, **kwargs)
    print(f"{Colors.YELLOW}[WARNING]{Colors.RESET} {text}")


def print_error(message, lang=None, **kwargs):
    if lang is None:
        lang = settings.LANGUAGE
    text = get_text(message, lang, **kwargs)
    print(f"{Colors.RED}[ERROR]{Colors.RESET} {text}")


def print_debug(message, debug=False):
    if debug:
        print(f"{Colors.MAGENTA}[DEBUG]{Colors.RESET} {message}")


def print_title(title):
    print(f"{Colors.CYAN}{Colors.BOLD}--- {title} ---{Colors.RESET}")


def print_line():
    print(f"{Colors.CYAN}--------------------------------{Colors.RESET}")