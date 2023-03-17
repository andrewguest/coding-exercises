var fib_seq: [Int] = [1, 2]  // Fibonacci sequence, starting with it's first two values


while fib_seq.max()! < 4000000 {  // while the max() value of "fib_seq" is less than 4,000,000

    let last_two_elements: [Int] = Array(fib_seq.suffix(2))  // create an array containing only the last two elements


    let next_value = last_two_elements[0] + last_two_elements[1]  // Sum the last two values of "fib_seq" to get the next value

    if next_value < 4000000 {
        fib_seq.append(next_value)  // add to the fib_seq array
    } else {
        break  // break out of the loop when we've reached 4,000,000 or more
    }
}

let even_fib_seq: [Int] = fib_seq.filter { $0 % 2 == 0 }  // array of only the even Fibonacci numbers
let total = even_fib_seq.reduce(0, +)  // sum all of the elements of "even_fib_seq"

print(total)