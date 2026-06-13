# Given an input string s consisting solely of the characters '(', ')', '{', '}', '[' and ']', determine whether s is a valid string. A string is considered valid if every opening bracket is closed by a matching type of bracket and in the correct order, and every closing bracket has a corresponding opening bracket of the same type.

# Example 1:

# Inputs:

# s = "(){({})}"
# Output:

# True
# Example 2:

# Inputs:

# s = "(){({}})"
# Output:

# False

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {")":"(", "]":"[", "}":"{"}
        stack = []
        opens = set(["{", "(", "["])
        for c in s:
            if c in opens:
                stack.append(c)
            else:
                if len(stack) == 0 or mapping[c] != stack.pop():
                    return False
        if len(stack) != 0:
            return False
        return True

print(Solution().isValid("(){({})}"))
print(Solution().isValid("(){({}})"))
