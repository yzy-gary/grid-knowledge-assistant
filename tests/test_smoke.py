from grid_knowledge_assistant import normalize_question


def test_normalize_question_strips_whitespace() -> None:
    assert normalize_question("  how many substations?  ") == "how many substations?"
