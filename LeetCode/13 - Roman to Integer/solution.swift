class Solution {
    func romanToInt(_ s: String) -> Int {

        var s2 = s
        var total = 0
        let combo_symbols_to_values = [
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        ]
        let symbol_to_values = [
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        ]

        // Check for any combo_symbols_to_values keys in "s" and add their values to "total" (if any symbols are found)
        for (symbol, value) in combo_symbols_to_values {
            if s2.contains(symbol) {
                total += value
                s2 = s2.replacingOccurrences(of: symbol, with: "")
            }
        }

        // After checking for combo symbols and removing them, do the same thing with the keys from symbol_to_values
        for char in s2 {
            total += symbol_to_values[String(char)]!
        }

        return total
    }
}