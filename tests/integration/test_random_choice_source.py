from rock_paper_scissors.domain.choice import Choice
from rock_paper_scissors.infrastructure.random_choice_source import RandomChoiceSource


def test_random_choice_source_only_returns_valid_choices() -> None:
    source = RandomChoiceSource()

    drawn = {source.next_choice() for _ in range(200)}

    assert drawn <= set(Choice)
    assert drawn == set(Choice)
