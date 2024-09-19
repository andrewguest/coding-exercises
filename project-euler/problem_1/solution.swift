var current_number: Int = 0
var total: Int = 0

while current_number < 1000 {
    if (current_number % 3 == 0) || (current_number % 5 == 0) {
        total += current_number
    }

    current_number += 1
}

print(total)