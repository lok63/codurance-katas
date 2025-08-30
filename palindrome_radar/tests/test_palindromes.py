import pytest

from palindrome_radar.src.palindrome_checker import PalindromeChecker
from palindrome_radar.src.pre_processors import BasicPreprocessor, SpacyPreprocessor


class TestPalindromeDetection:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.palindrome_radar = PalindromeChecker(BasicPreprocessor())

    @pytest.mark.parametrize(
        "sample, expected",
        [
            ("apa", True),
            ("anna", True),
            ("anna!", True),
            ("race car", True),
            ("race car1", False),
            ("Race car", True),
            ("A man, a plan, a canal, Panama!", True),
            ("axDbTbd6", False),
            ("6axDbTbd6", False),
            ("Hello, World!", False),
            ("ann-a", True),
        ],
    )
    def test_palindromes(self, sample: str, expected: bool):
        actual = self.palindrome_radar.is_palindrome(sample)
        assert actual == expected
