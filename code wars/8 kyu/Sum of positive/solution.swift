func sumOfPositives (_ numbers: [Int] ) -> Int {
    var total: Int = 0

    for n in numbers {
        if n > 0 {
            total += n
        }
    }

    return total
}