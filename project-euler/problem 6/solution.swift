
// Array(1...100)  -> create an array of numbers 1 to 100 (inclusive)
// .map { $0 * $0 }  -> map each element in the array to the closure where we're squaring each element
var sum_of_squares: [Int] = Array(1...100).map { $0 * $0 }

// .reduce(0, +)  -> reduce the array to an integer by adding (+) each element together and starting with 0
var sum_of_squares_total: Int = sum_of_squares.reduce(0, +)


// .reduce(0, +)  -> reduce the array to an integer by adding (+) each element together and starting with 0
var square_of_sums: Int = Array(1...100).reduce(0, +)

// square the integer by multiplying it by itself
var square_of_sums_total = square_of_sums * square_of_sums



print(square_of_sums_total - sum_of_squares_total)