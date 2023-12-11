class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        # nums[:]  -> replace a list in place
        nums[:] = sorted(set(nums))

        return len(nums)
