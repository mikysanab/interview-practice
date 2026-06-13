# Given an encoded string, write a function to return its decoded string that follows a specific encoding rule: k[encoded_string], where the encoded_string within the brackets is repeated exactly k times. Note that k is always a positive integer. The input string is well-formed without any extra spaces, and square brackets are properly matched. Also, assume that the original data doesn't contain digits other than the ones that specify the number of times to repeat the following encoded_string.

# Inputs:

# s = "3[a2[c]]"
# Output:

# "accaccacc"


#s = "3[a2[c]]2[a]"

class Solution:
    def decodeString(self, s: str) -> str:
        # Your code goes here
        stack = []
        current_string = ""
        current_count = 0
        for c in s:
            if c == "[":
                stack.append(current_string)
                stack.append(current_count)
                current_count = 0
                current_string = ""
            elif c == "]":
                count = stack.pop()
                prev_string = stack.pop()
                current_string = prev_string + count*current_string
            elif c.isdigit():
                current_count = current_count*10 + int(c)
            else:
                current_string += c
        return current_string
