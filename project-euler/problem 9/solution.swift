for a: Int in 1...1000 {
    for b: Int in a...1000 {
        for c: Int in b...1000 {
            if a + b + c == 1000 {
                if (a*a) + (b*b) == c*c {
                    print("A: \(a) B: \(b) C: \(c)")
                    print("Product is: \(a*b*c)")

                    break  // if the solution if found, break out of the loops to save time
                }
            }
        }
    }
}