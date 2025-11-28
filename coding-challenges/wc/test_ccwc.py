from ccwc import count_bytes, count_words, count_lines, count_characters


def test_count_bytes():
    assert count_bytes(filename="test.txt") == 342190


def test_count_lines(filename="test.txt"):
    assert count_lines(filename="test.txt") == 7145


def test_count_words():
    assert count_words(filename="test.txt") == 58164


def test_count_characters():
    # 339292 is the expected value if the locale supports multibyte characters
    # 342190 is the expected value if the locale does NOT support multibyte characters
    assert (
        count_characters(filename="test.txt") == 342190
        or count_characters(filename="test.txt") == 339292
    )
