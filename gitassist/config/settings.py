"""Global configuration settings for GitAssist."""

import os
import sys

APP_NAME = "GitAssist"
APP_VERSION = "0.1.0"
DEBUG = False
LOG_FILE = os.path.join(os.path.expanduser("~"), ".gitassist.log")
DEFAULT_LANGUAGE = "en"
LANGUAGE = "en"
DRY_RUN = "--dry-run" in sys.argv

# AI Provider settings
AI_PROVIDER = "rule_based"  # options: rule_based, ollama, openai
AI_ENABLED = False           # kept for backward compatibility, use AI_PROVIDER now
AI_API_KEY = ""              # for OpenAI
AI_MODEL = "gpt-3.5-turbo"   # for OpenAI

OLLAMA_BASE_URL = "http://localhost:11434"
OLLAMA_MODEL = "llama3.2"