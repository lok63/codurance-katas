import pytest

from leap_year.src.leap_year_checker import LeapYearChecker


class TestLeapYearChecker:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.leap_year_checker = LeapYearChecker()

    @pytest.mark.parametrize(
        "year, expected",
        [
            (1997, False),
            (1996, True),
            (1600, True),
            (1800, False),
            (2000, True),
            (1900, False),
            (2004, True),
            (2100, False),
            (2400, True),
            (1999, False),
            (2001, False),
            (1700, False),
            (800, True),
        ],
        ids=[
            "1997 - Not divisible by 4",
            "1996 - Divisible by 4",
            "1600 - Divisible by 400",
            "1800 - divisible by 4, divisible by 100, NOT divisible by 400",
            "2000 - Divisible by 400",
            "1900 - Divisible by 100 but not 400",
            "2004 - Divisible by 4",
            "2100 - Divisible by 100 but not 400",
            "2400 - Divisible by 400",
            "1999 - Not divisible by 4",
            "2001 - Not divisible by 4",
            "1700 - Divisible by 100 but not 400",
            "800 - Divisible by 400",
        ]
    )
    def test_is_leap_year(self, year:int, expected:bool):
        actual =  self.leap_year_checker.is_leap_year(year)
        assert actual == expected
