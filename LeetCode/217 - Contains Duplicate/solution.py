class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        """Check the length of `nums` as a list to the length of `nums` as a set.
        If there's a difference that means there were duplicates in the list
            version and we return the opposite boolean, because duplicates are
            a good thing in this problem.

        Args:
            nums (list[int]): The list of numbers to check for duplicates

        Returns:
            bool: If `nums` contains any duplicates
        """
        return not len(set(nums)) == len(nums)
