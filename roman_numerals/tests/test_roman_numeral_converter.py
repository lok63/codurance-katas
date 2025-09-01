import pytest

from roman_numerals.src.roman_numerals_converter import RomanNumeralsConverter


class TestRomanNumeralConverter:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.converter = RomanNumeralsConverter()

    @pytest.mark.parametrize(
        "number, expected",
        [
            (1, "I"),
            (5, "V"),
            (10, "X"),
            (50, "L"),
            (100, "C"),
            (500, "D"),
            (1000, "M"),
            # Unit place numbers
            (2, "II"),
            (3, "III"),
            (4, "IV"),
            (6, "VI"),
            (7, "VII"),
            (8, "VIII"),
            (9, "IX"),
            # Non  Unit place numbers
            (11, "XI"),
            (12, "XII"),
            (13, "XIII"),
            (14, "XIV"),
            (15, 'XV'),
            (16, 'XVI'),
            (17, 'XVII'),
            (18, 'XVIII'),
            (19, 'XIX'),
            (20, "XX"),
            (40, "XL"),
            (90, "XC"),
            (400, "CD"),
            (900, "CM"),
            (1994, "MCMXCIV"),
        ],
    )
    def test_convert(self, number: int, expected: str):
        actual = self.converter.convert(number)
        assert actual == expected
