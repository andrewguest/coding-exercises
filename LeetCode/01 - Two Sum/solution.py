class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        # dictionary to hold the number and it's index
        # {number: index, number2: index2}
        solution_dict: dict[int, int] = {}

        # loop through the index and value of nums
        for i, value in enumerate(nums):
            remaining = target - value

            # if the remaining amount (after subtracting the current "value" from "target") is in solution_dict already
            #   then get it's index and return the current index (i) and the index that you got from solution_dict
            if remaining in solution_dict:
                return [i, solution_dict[remaining]]

            # if no solution was found this try, then add "value" and "i" to solution_dict before moving on to the
            #   next loop iteration
            solution_dict[value] = i

        return []
