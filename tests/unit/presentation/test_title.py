from rock_paper_scissors.presentation.shared import title


def test_colorize_title_disabled_returns_plain() -> None:
    assert title.colorize_title(enabled=False) == title.TITLE


def test_colorize_title_enabled_colors_each_word() -> None:
    out = title.colorize_title(enabled=True)

    for color in title.TITLE_COLORS:
        assert color in out
    assert out.count(title.RESET) == len(title.TITLE.strip().splitlines())
