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
        """Most Pythonic way"""
        return word == word[::-1]

    # @staticmethod
    # def efficient_palindrome(word: str) -> bool:
    #     """
    #     Useful for long strings by using 2 pointers.
    #     """
    #     left, right = 0, len(word) - 1
    #     while left < right:
    #         if word[left] != word[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #     return True

    @staticmethod
    def ef_palindrome(word: str) -> bool:
        """
        word: apa
        :param word:
        :return:
        """
        left, right = 0, len(word) - 1
        # we want to compare if the left-most and right-most character if they are the same
        # this is efficient because we can exit earlier if the word is a long one
        while left <= right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True

    def is_palindrome(self, word: str) -> bool:
        clean_word = self.pre_processor.pre_process(word)
        return self.ef_palindrome(clean_word)


if __name__ == "__main__":
    palindrome_checker = PalindromeChecker(SpacyPreprocessor())
    result = palindrome_checker.is_palindrome("ii")
    assert result == True
