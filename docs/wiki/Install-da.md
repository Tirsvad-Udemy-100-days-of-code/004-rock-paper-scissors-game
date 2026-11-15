[English](Install) · **Dansk** · [Bahasa Melayu](Install-ms)

# Installation

## Krav

- Python 3.13 eller nyere
- Ingen afhængigheder i drift; `pytest`, `ruff` og `mypy` installeres til udvikling

## Trin

Opret og aktivér et virtuelt miljø i `.venv`:

```bash
python -m venv .venv
```

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux / Git Bash
source .venv/bin/activate
```

Installér projektet i redigerbar tilstand med udviklingsværktøjerne:

```bash
python -m pip install -e ".[dev]"
```

Forlad miljøet med `deactivate`. Næste: [Spil](Play-da).
