class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        # if the target is in nums then get the index of target
        if target in nums:
            return nums.index(target)

        # add target to nums, sort nums, and then get the index of target
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
