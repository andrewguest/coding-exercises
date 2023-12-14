class Solution {
    func searchInsert(_ nums: [Int], _ target: Int) -> Int {

        // return index value of the first occurance of target
        if nums.contains(target) {
            return nums.firstIndex(of: target)!
        } else {
            // nums is a constant, so we cannot manipulate it, so we create a mutable copy of it and manipulate that instead
            var temp_nums: [Int] = nums

            temp_nums.append(target)  // add target to nums
            temp_nums.sort()  // sort nums so that the new target value is in the correct index
            return temp_nums.firstIndex(of: target)!
        }
    }
}