class Solution {
    func isValid(_ s: String) -> Bool {
        var stack: [String.Element] = []

        for c in s {
            if c == "(" {
                stack.append(")")
            } else if c == "[" {
                stack.append("]")
            } else if c == "{" {
                stack.append("}")
            } else {
                if let bracket = stack.last, bracket == c {
                    stack.popLast()
                } else {
                    return false
                }
            }
        }

        return stack.isEmpty
    }
}