from kerbalforge.parser.tokenizer import Tokenizer, TokenType


def test_left_brace():
    tokenizer = Tokenizer("{")

    tokens = tokenizer.tokenize()

    assert tokens[0].type is TokenType.LBRACE
