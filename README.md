# 🚀 Rock Paper Scissors Game

A beginner-friendly Python program to play Rock, Paper, Scissors against the computer (Udemy's *100 Days of Code™: The Complete Python Pro Bootcamp*, Day 4).

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

You choose `0` (Rock), `1` (Paper) or `2` (Scissors); the computer picks randomly using the `random` module. Both choices are shown as ASCII art, and the winner is decided with `if`/`elif`/`else` logic (rock beats scissors, scissors beats paper, paper beats rock). Draws and invalid input are handled.

![Screenshot of the game](docs/screenshot.png)

The repository holds the game in `src/rock_paper_scissors/`, its tests in `tests/`, and the project documents in `docs/`, which follow the SQA and QC framework in `framework/`.

## 📋 Requirements

- Python 3.13 or newer
- No runtime dependencies
- [pytest](https://pytest.org) for running the tests (installed via the `dev` extra)

## 🛠️ Setup

Create and activate a local virtual environment in `.venv`:

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (cmd)
.venv\Scripts\activate.bat

# macOS / Linux / Git Bash
source .venv/bin/activate        # Git Bash on Windows: source .venv/Scripts/activate
```

Install the project in editable mode with test tools:

```bash
python -m pip install -e ".[dev]"
```

Leave the environment with `deactivate`.

## ▶️ Run

With the virtual environment active:

```bash
python -m rock_paper_scissors
```

or, after installing, `rock-paper-scissors`.

## 🧪 Tests

```bash
python -m pytest
```

## 📄 License

GNU Affero General Public License v3.0 or later (AGPL-3.0-or-later). See [LICENSE](./LICENSE).

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/004-rock-paper-scissors-game
[documentation]: ./docs/
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/004-rock-paper-scissors-game/issues
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[TM-001]: ./docs/sqa/traceability-matrix.md
