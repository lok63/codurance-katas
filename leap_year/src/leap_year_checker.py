
class LeapYearChecker:

    def is_leap_year(self, year: int) -> bool:
        if not self.__is_divisible_by_4(year):
            return False

        if self.__is_divisible_by_4(year) and self.__is_divisible_by_100(year) and not self.__is_divisible_by_400(year):
            return False

        if self.__is_divisible_by_4(year) or self.__is_divisible_by_400(year):
            return True

        return False

    @staticmethod
    def __is_divisible_by_4(year: int) -> bool:
        return year % 4 is 0

    @staticmethod
    def __is_divisible_by_100(year: int) -> bool:
        return year % 100 is 0

    @staticmethod
    def __is_divisible_by_400(year: int) -> bool:
        return year % 400 is 0

