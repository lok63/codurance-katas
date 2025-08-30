import pytest
from palindrome_radar.src.pre_processors import BasicPreprocessor, SpacyPreprocessor


class TestBasicPreprocessor:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.pre_processor = BasicPreprocessor()

    @pytest.mark.parametrize(
        "word,expected",
        [
            ("apa", "apa"),
            ("Anna", "anna"),
            ("anNa!", "anna!"),
            ("axDbTbd6", "axdbtbd6"),
        ],
    )
    def test_lower_case(self, word, expected):
        actual = self.pre_processor.lower_case(word)
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
    def test_punctuation(self, word, expected):
        actual = self.pre_processor.remove_punctuation(word)
        assert actual == expected
