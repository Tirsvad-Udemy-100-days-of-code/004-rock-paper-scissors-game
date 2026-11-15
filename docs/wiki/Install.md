**English**

# Install

## Requirements

- Python 3.13 or newer
- No runtime dependency; `pytest`, `ruff` and `mypy` are installed for development

## Steps

Create and activate a virtual environment in `.venv`:

```bash
python -m venv .venv
```

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux / Git Bash
source .venv/bin/activate
```

Install the project in editable mode with the development tools:

```bash
python -m pip install -e ".[dev]"
```

Leave the environment with `deactivate`. Next: [Play](Play).
