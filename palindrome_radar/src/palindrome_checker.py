from palindrome_radar.src.pre_processors import (
    AbstractPreprocessor,
    BasicPreprocessor,
    SpacyPreprocessor,
)


class PalindromeChecker:
    def __init__(self, pre_processor: AbstractPreprocessor):
        self.pre_processor = pre_processor

    @staticmethod
    def pythonic_palindrome(word: str) -> bool:
        """Most Pythonic way using string slicing"""
        return word == word[::-1]

    @staticmethod
    def efficient_palindrome(word: str) -> bool:
        """
        Check if a word is a palindrome using two-pointer technique.

        This approach is more memory and time efficient than string slicing methods,
        especially for long strings ( given that they  because:

        Memory efficiency:
        - Uses O(1) extra memory (only two integer pointers)
        - No additional string copies are created
        - String slicing creates O(n) memory overhead for the reversed copy

        Time efficiency:
        - Early termination: stops immediately upon finding first character mismatch
        - Best case O(1) when first/last characters differ

        For very long strings or performance-critical applications, this can provide
        significant speedup and memory savings compared to word == word[::-1].
        """
        left, right = 0, len(word) - 1
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True

    def is_palindrome(self, word: str) -> bool:
        clean_word = self.pre_processor.pre_process(word)
        return self.efficient_palindrome(clean_word)


if __name__ == "__main__":
    palindrome_checker = PalindromeChecker(BasicPreprocessor())
    result = palindrome_checker.is_palindrome("ii")
    assert result == True
