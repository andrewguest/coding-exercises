from wc_py.wc_py import PythonWC


def test_byte_count():
    """Test that the `-c` and `--bytes` flags return `342190`"""

    # Test with the short flag
    wc = PythonWC(["-c", "test.txt"])
    assert wc.count_bytes() == 342190

    # Test with the long flag
    wc = PythonWC(["--bytes", "test.txt"])
    assert wc.count_bytes() == 342190


def test_line_count():
    """Test that the `-l` and `--lines` flags return `7145`"""

    # Test with the short flag
    wc = PythonWC(["-l", "test.txt"])
    assert wc.count_lines() == 7145

    # Test with the long flag
    wc = PythonWC(["--lines", "test.txt"])
    assert wc.count_lines() == 7145


def test_word_count():
    """Test that the `-w` and `--words` flags return `58164`"""

    # Test with the short flag
    wc = PythonWC(["-w", "test.txt"])
    assert wc.count_words() == 58164

    # Test with the long flag
    wc = PythonWC(["--words", "test.txt"])
    assert wc.count_words() == 58164


def test_character_count():
    """Test that the `-m` and `--chars` flags return `339292`"""

    # Test with the short flag
    wc = PythonWC(["-m", "test.txt"])
    assert wc.count_characters() == 339292

    # Test with the long flag
    wc = PythonWC(["--chars", "test.txt"])
    assert wc.count_characters() == 339292


def test_default_no_options():
    """Test that, if no CLI options are provided then the program outputs the
    equivalent of `-c`, `-l` and -`w` options"""

    wc = PythonWC(["test.txt"])
    assert wc.default_options() == "7145 58164 342190 test.txt"
    