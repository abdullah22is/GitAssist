"""Command safety analyzer."""

import re
from gitassist.security.risk import RiskLevel
from gitassist.localization.texts import get_text


DANGEROUS_PATTERNS = [
    {
        "pattern": r"^git\s+reset\s+--hard",
        "level": RiskLevel.DANGEROUS,
        "warning_key": "warning_reset_hard",
        "alternative_key": "alternative_reset_hard",
    },
    {
        "pattern": r"^git\s+push\s+.*--force",
        "level": RiskLevel.DANGEROUS,
        "warning_key": "warning_force_push",
        "alternative_key": "alternative_force_push",
    },
    {
        "pattern": r"^git\s+clean\s+-fd",
        "level": RiskLevel.DANGEROUS,
        "warning_key": "warning_clean_fd",
        "alternative_key": "alternative_clean_fd",
    },
    {
        "pattern": r"^git\s+checkout\s+--\s+\.?",
        "level": RiskLevel.DANGEROUS,
        "warning_key": "warning_checkout_discard",
        "alternative_key": "alternative_checkout_discard",
    },
    {
        "pattern": r"^git\s+rebase\s+-i\s+HEAD~",
        "level": RiskLevel.DANGEROUS,
        "warning_key": "warning_rebase_i",
        "alternative_key": "alternative_rebase_i",
    },
    {
        "pattern": r"^git\s+branch\s+-D",
        "level": RiskLevel.CAUTION,
        "warning_key": "warning_branch_D",
        "alternative_key": "alternative_branch_D",
    },
    {
        "pattern": r"^git\s+merge",
        "level": RiskLevel.CAUTION,
        "warning_key": "warning_merge",
        "alternative_key": "alternative_merge",
    },
    {
        "pattern": r"^git\s+stash\s+drop",
        "level": RiskLevel.CAUTION,
        "warning_key": "warning_stash_drop",
        "alternative_key": "alternative_stash_drop",
    },
]


def analyze_command(command_list):
    """Return (risk_level, warning_text, alternative_text)."""
    cmd_str = " ".join(command_list).strip()

    for entry in DANGEROUS_PATTERNS:
        if re.match(entry["pattern"], cmd_str, re.IGNORECASE):
            warning = get_text(entry["warning_key"])
            alternative = get_text(entry["alternative_key"]) if entry.get("alternative_key") else ""
            return entry["level"], warning, alternative

    return RiskLevel.SAFE, "", ""