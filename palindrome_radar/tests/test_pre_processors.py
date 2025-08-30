import pytest
from palindrome_radar.src.pre_processors import BasicPreprocessor, SpacyPreprocessor


@pytest.mark.parametrize("preprocessor_class", [BasicPreprocessor, SpacyPreprocessor])
class TestPreprocessors:
    @pytest.fixture
    def preprocessor(self, preprocessor_class):
        return preprocessor_class()

    @pytest.mark.parametrize(
        "word,expected",
        [
            ("apa", "apa"),
            ("Anna", "anna"),
            ("anNa!", "anna!"),
            ("axDbTbd6", "axdbtbd6"),
        ],
    )
    def test_lower_case(self, preprocessor, word, expected):
        actual = preprocessor.lower_case(word)
        assert actual == expected

    @pytest.mark.parametrize(
        "word, expected",
        [
            ("Race car", "Racecar"),
            ("A man, a plan, a canal, Panama!", "AmanaplanacanalPanama"),
            ("axDbTbd6", "axDbTbd6"),
            ("Hello, World!", "HelloWorld"),
            ("ann-a", "anna"),
        ],
    )
    def test_remove_punctuation(self, preprocessor, word, expected):
        actual = preprocessor.remove_punctuation(word)
        assert actual == expected

    @pytest.mark.parametrize(
        "word, expected",
        [
            ("Race car", "racecar"),
            ("A man, a plan, a canal, Panama!", "amanaplanacanalpanama"),
            ("Hello, World!", "helloworld"),
            ("ann-a", "anna"),
        ],
    )
    def test_pre_process(self, preprocessor, word, expected):
        actual = preprocessor.pre_process(word)
        assert actual == expected
