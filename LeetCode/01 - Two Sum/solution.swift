class Solution {

    func twoSum(_ nums: [Int], _ target: Int) -> [Int] {

        // dictionary to hold any already tested values
        // [number: index, number: index]
        var solution_dict = [Int: Int]()

        // loop through "nums" by index and value
        for (index, number) in nums.enumerated() {
            var remaining_value = target - number

            if let lastIndex = solution_dict[target - number] {
                return [index, lastIndex]
            }

            // add to the dictionary if the solution wasn't found in this iteration of the loop
            solution_dict[number] = index
        }

        return []
    }

}
