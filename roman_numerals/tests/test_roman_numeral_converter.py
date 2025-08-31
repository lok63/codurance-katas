import pytest

from roman_numerals.src.roman_numerals_converter import RomanNumeralsConverter


class TestRomanNumeralConverter:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.converter = RomanNumeralsConverter()

    @pytest.mark.parametrize(
        "number, expected",
        [
            (1, 'I'),
            (2, 'II'),
            (3, 'III'),
            # (4, 'IV'),
            (5, 'V'),
            (6, 'VI'),
            (7, 'VII'),
            (8, 'VIII'),
            # (9, 'IX'),
        ]
    )
    def test_convert(self, number: int, expected: str):
        actual = self.converter.convert(number)
        assert actual == expected


    @pytest.mark.parametrize(
        "number, expected",
        [
            (1, {"I" : 1}),
            (2, {"I" : 1}),
            (3, {"I" : 1}),
            (4, {"I" : 1, "V":5}),
            (5, {"I" : 1, "V":5}),
            (6, {"I" : 1, "V":5}),
            (7, {"I" : 1, "V":5}),
            (8, {"I" : 1, "V":5}),
            # (9, 'IX'),
        ]
    )
    def test_latin_candidates_to_use(self,number: int, expected: str):
        actual = self.converter.find_latin_character_candidates(number)
        actual == expected