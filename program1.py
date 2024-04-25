class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map:
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            # If the character is neither an opening nor a closing bracket, skip it
            else:
                continue
        
        # After iterating through all characters, if the stack is empty, return True (all brackets are valid)
        return not stack
