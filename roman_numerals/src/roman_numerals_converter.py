class RomanNumeralsConverter:

    def convert(self, amount: int) -> str:
        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

        result = ""
        for value, numeral in values:
            count = amount // value
            if count != 0:
                result += numeral * count
                # substruct from the original amount the numer we just used
                # i.e. if input is 11, then we printed X and now we want to remove the 10
                # i.e. if input is 20, then we printed 2 Xs and now we want to remove them all together
                amount -= value * count
        return result


if __name__ == "__main__":
    converter = RomanNumeralsConverter()
    print(converter.convert(11))
