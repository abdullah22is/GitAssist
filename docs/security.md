# GitAssist Security Model

## Core Security Rule

**Never execute an unvalidated command directly.**

All Git operations, whether from menus or manual input, must pass through a validation pipeline before execution.

## Pipeline Stages

1. **Context Check** (`security/context.py`): Verifies that the command is appropriate for the current repository state.  
   - Example: Prevents merging with uncommitted changes.
   - Example: Prevents pushing without a remote.

2. **Safety Analysis** (`security/analyzer.py`): Classifies the command into risk levels:
   - `SAFE`
   - `CAUTION`
   - `DANGEROUS`

   For risky commands, warnings and safer alternatives are displayed.

3. **User Confirmation**: For CAUTION/DANGEROUS commands, explicit confirmation is required.  
   - The user can cancel at any time.

4. **Execution** (`git/executor.py`): If approved, the command runs via `subprocess` with list arguments (no shell injection).  
   - `--dry-run` mode simulates execution without actually running anything.

5. **Error Intelligence** (`errors/analyzer.py`): After a failure, known errors are explained with practical suggestions.

## Risk Classification Examples

| Command | Risk Level |
|---------|------------|
| `git status` | SAFE |
| `git branch -d feature` | CAUTION |
| `git merge feature` | CAUTION |
| `git reset --hard` | DANGEROUS |
| `git push --force` | DANGEROUS |

## Protecting Secrets

- GitHub tokens entered for API operations are used only in memory and never written to logs or configuration files.
- Logging is designed to avoid recording sensitive data (tokens, passwords).

## Limitations

- The current implementation uses `subprocess.run` with list arguments, which is safe from shell injection.  
- However, the safety analyzer relies on pattern matching; complex edge cases might not be covered. Future improvements could include a more robust command parser.
- The tool trusts the local Git installation; it does not verify the integrity of Git itself.

## Best Practices

- Always run in `--dry-run` mode when trying unfamiliar commands.
- Review warnings and alternatives before proceeding.
- Use a dedicated GitHub token with minimal permissions (repo scope only).