class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0

        # dictionaries for converting the Roman Numerals to their values
        combo_symbols_to_values = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        symbol_to_values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        for symbol, value in combo_symbols_to_values.items():
            # loop through the symbols in combo_symbols_to_values and check if any of them are in "s"
            if symbol in s:
                # if a symbol is found in "s", add it's value to "total" and strip that symbol from "s"
                total += value
                s = s.replace(symbol, "")

        for char in s:
            total += symbol_to_values[char]

        return total
