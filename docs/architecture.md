# GitAssist Architecture

## Overview
GitAssist is a modular command-line assistant that wraps Git operations with safety, context awareness, and error intelligence.

## High-Level Components

- **CLI Layer** (`gitassist/cli/`): Handles user input, output formatting, and interactive menus.
- **Core Layer** (`gitassist/core/`): Coordinates workflows, submenus, and manual command mode.
- **Git Layer** (`gitassist/git/`): Provides controlled execution of Git commands and repository state inspection.
- **Security Layer** (`gitassist/security/`): Analyzes commands for risk, context appropriateness, and safer alternatives.
- **Error Layer** (`gitassist/errors/`): Interprets common Git errors and provides actionable suggestions.
- **GitHub Integration** (`gitassist/github/`): Parses remote URLs and interacts with GitHub API.
- **Logging** (`gitassist/logging/`): Records operations to a log file.
- **Config** (`gitassist/config/`): Central settings, including dry-run mode.

## Data Flow

1. `__main__.py` initializes the environment and enters the main loop.
2. `core/menu.py` displays a dynamic menu based on `git/repository.py` state.
3. User selects an action or enters a manual command.
4. Core commands call specific modules (`git/branches.py`, `git/stash.py`, `git/sync.py`, etc.) which build commands.
5. All executions go through `git/executor.run_git_command()`.
6. The executor performs context check, safety analysis, dry-run handling, then runs the command via `subprocess`.
7. After execution, errors are analyzed and logged.
8. `core/suggestions.py` provides next-step recommendations.

## Design Principles

- **Safety-first**: No command is executed without validation.
- **Context-aware**: Menus and checks adapt to repository state.
- **Modularity**: Each concern is separated into its own package.
- **Extensibility**: Adding new Git features is a matter of adding new modules and menu entries.
- **Localization-ready**: Although currently English-only, text is centralized in `cli/output.py` and can be moved to a locale system later.

## Testing

Unit tests are located in `tests/` and run with:
```bash
python -m unittest discover -s tests 
Future Enhancements
AI-powered suggestions (optional layer).

Full localization (Arabic/English).

GUI version.

More sophisticated command parser and risk engine.