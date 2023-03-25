class Solution(object):
	def isValid(self, s):
        """
        Args:
            s (str): String to check

        Returns:
            bool: Is the string valid
        """

        # Filter out odd length strings, since they should always return False
        if len(s) % 2 != 0:
            return False

        # Valid characters and their companion character
        brackets = {'(':')', '{':'}','[':']'}

        stack = []
        for character in s:  # loop through 's'
            if character in brackets:  # check if 'character' is a key in the 'brackets' dictionary
                stack.append(character)  # append 'character' to 'stack'
            elif len(stack) == 0 or brackets[stack.pop()] != character:  # 1
                return False
        return len(stack) == 0 # 2
	
# 1. else if it's the right bracket and the stack is empty(meaning no matching left bracket), or the left bracket doesn't match
# 2. finally check if the stack still contains unmatched left bracket