import os
import subprocess
import sys
from pathlib import Path

import pytest

from rock_paper_scissors.infrastructure import bootstrap

SOURCE_FOLDER = Path(__file__).resolve().parents[2] / "src"


def test_invalid_input_prints_a_message(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "9")

    bootstrap.main()

    assert "invalid" in capsys.readouterr().out


def test_non_numeric_input_prints_a_message(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setattr("builtins.input", lambda _: "rock")

    bootstrap.main()

    assert "invalid" in capsys.readouterr().out


@pytest.mark.parametrize(
    ("typed", "computer", "message"),
    [("0", 2, "You win!"), ("0", 1, "You lose!"), ("1", 1, "It's a draw!")],
)
def test_a_round_shows_both_choices_and_the_result(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    typed: str,
    computer: int,
    message: str,
) -> None:
    monkeypatch.setattr("builtins.input", lambda _: typed)
    monkeypatch.setattr("random.randint", lambda a, b: computer)

    bootstrap.main()

    out = capsys.readouterr().out
    assert "You chose" in out
    assert "Computer chose" in out
    assert message in out


def test_module_starts_the_game_from_the_command_line() -> None:
    completed = subprocess.run(
        [sys.executable, "-m", "rock_paper_scissors"],
        input="0\n",
        env={**os.environ, "PYTHONPATH": str(SOURCE_FOLDER)},
        capture_output=True,
        text=True,
        check=True,
    )

    assert "You chose Rock" in completed.stdout
