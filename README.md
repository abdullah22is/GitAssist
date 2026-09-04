# GitAssist

A smart and security-aware Git assistant that analyzes repository state, presents relevant actions, validates commands, and helps users work with Git safely.

![Version](https://img.shields.io/badge/version-0.1.0-blue)

## Features

- **Context-aware dynamic menu**: Only shows relevant actions based on repository state.
- **Safe execution**: All Git commands pass through validation, context check, risk analysis, and confirmation.
- **Risk levels**: SAFE, CAUTION, DANGEROUS with warnings and safer alternatives.
- **Manual command mode**: Enter any Git command; the tool analyzes it and warns if inappropriate or dangerous.
- **Typo detection**: Suggests corrections for common Git command typos.
- **Error intelligence**: Explains common Git errors and provides actionable suggestions.
- **Conflict detection**: After pull/merge, lists conflicted files and guides resolution.
- **File management**: Create, edit, delete files, and create directories.
- **Branch management**: List, create, switch, delete, merge branches.
- **Stash management**: Save, list, apply, pop, drop stashes.
- **Synchronization**: Fetch, pull, push, and check remote updates.
- **GitHub integration**: View remote details, open repo in browser, create repository via API.
- **Bilingual support**: English and Arabic.
- **Voice commands**: Optional voice input using speech recognition.
- **AI assistance**: Optional AI provider (Ollama local or OpenAI) for natural language understanding.
- **Dry-run mode**: `--dry-run` simulates commands without executing them.
- **Logging**: Records all operations to `~/.gitassist.log`.

## Installation

### Prerequisites
- Python 3.8+ (3.12 or 3.13 recommended for voice support)
- Git installed and in PATH

### Steps
```bash
git clone <repository-url>
cd GitAssist
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # Windows PowerShell
pip install -r requirements.txt
Note: Core functionality uses only Python standard library.
Optional voice/AI features require additional packages.
If you want to install them:

bash
pip install -r requirements-optional.txt
Usage
Run the interactive CLI:

bash
python -m gitassist
At startup, choose language:

English

العربية

Dry-run mode:

bash
python -m gitassist --dry-run
Voice Commands (Optional)
To enable voice commands, install:

bash
pip install SpeechRecognition sounddevice numpy
Then from the main menu choose v.
Speak a Git command like:

"git status"

"git log"

Note: Voice recognition uses Google Speech Recognition, which requires internet.
For offline voice recognition, you need to integrate another engine.

AI Assistance (Optional)
GitAssist has a built-in rule-based engine that understands common Arabic/English phrases without any API key.

Examples:

"انشاء مستودع جديد" → git init

"عرض الحالة" → git status

"حفظ التغييرات" → git add . && git commit

To enable advanced AI:

Ollama (local, free, no internet)
Install Ollama from https://ollama.com

Pull a model: ollama pull llama3.2

In settings.py:

python
AI_PROVIDER = "ollama"
OLLAMA_MODEL = "llama3.2"
OpenAI (requires API key)
Install: pip install openai

In settings.py:

python
AI_PROVIDER = "openai"
AI_API_KEY = "your-key"
AI_MODEL = "gpt-3.5-turbo"
Important: AI suggestions are never executed directly. They pass through the same safety pipeline, and you must confirm before execution.

Configuration
Language: Selected at startup, stored in settings.LANGUAGE.

Dry-run mode: Pass --dry-run as command-line argument.

Log file: ~/.gitassist.log

AI provider: Set AI_PROVIDER in config/settings.py (rule_based, ollama, openai).

Voice: Uses sounddevice and SpeechRecognition if installed.

Testing
Run unit tests:

bash
python -m unittest discover -s tests
Project Structure
text
GitAssist/
├── gitassist/
│   ├── __main__.py
│   ├── cli/
│   ├── core/
│   ├── git/
│   ├── security/
│   ├── errors/
│   ├── github/
│   ├── ai/
│   ├── logging/
│   ├── config/
│   └── localization/
├── tests/
├── docs/
├── README.md
└── LICENSE
Notes on Voice and AI
Voice commands require microphone access and internet for Google Speech Recognition.

The built-in rule engine works offline and supports common Arabic/English phrases.

Ollama AI works completely offline after model download.

OpenAI AI requires an API key and internet connection.

AI is optional; the core Git features work without any AI or voice dependencies.

AI suggestions are suggestions only — never executed without confirmation.

No tokens or API keys are stored in logs.

Voice support depends on numpy, sounddevice, and SpeechRecognition. If they are not installed, the voice feature is disabled gracefully.

Troubleshooting
PyAudio errors
Use sounddevice instead of PyAudio to avoid C++ build tools. If you see errors about PyAudio, ensure you have installed sounddevice and numpy, not PyAudio.

numpy not available for Python 3.14
If you are using Python 3.14 and cannot install numpy, switch to Python 3.12 or 3.13 for voice support. Core Git features still work without numpy.

AI not generating commands
For rule-based AI: check the phrase matches common patterns in gitassist/ai/fallback.py.

For Ollama: ensure Ollama is running (ollama serve) and model is pulled.

For OpenAI: check API key and internet connection.

Contributing
Contributions are welcome! Please open an issue first to discuss your ideas.

License
MIT License. See LICENSE.