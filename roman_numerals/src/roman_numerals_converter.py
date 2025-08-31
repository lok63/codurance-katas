from enum import Enum
from typing import Dict
class Arithmoi(str, Enum):
    monades = "I"
    dekades = "V"



class RomanNumeralsConverter:

    roman_map = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000,
    }

    def find_latin_character_candidates(self, inp: int) -> Dict[str, int]:
        characters_to_use = {}

        for k ,v in self.roman_map.items():
            if inp % v==0:
                characters_to_use[k]=v
            else:
                break
        return characters_to_use

    def convert(self, inp: int) -> str:

        characters_to_use = []
        result = ""

        characters_to_use = self.find_latin_character_candidates(inp)

        number_to_use = characters_to_use[-1][1]

        while number_to_use !=0:
            for tup in characters_to_use[::-1]:
                how_many_times = number_to_use // tup[1]
                number_to_use = inp % tup[1]
                result = result.join(tup[0]*how_many_times)

        return result



if __name__ == '__main__':
    converter = RomanNumeralsConverter()
    print(converter.convert(4))