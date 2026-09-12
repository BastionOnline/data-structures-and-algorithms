class Solution:
    def isValid(self, s: str) -> bool:
        # make dict to store open and closed
        closingBrackets = {"}" : "{", ")":"(", "]":"["}
        stack = []

        # for each character in the string
        for char in s:
            # if it is in the closing
            if char in closingBrackets:
                # make sure there is value in stack; if stack
                # compare to last item in stack; stack[-1]
                if stack and stack[-1] == closingBracket[char]:
                    stack.pop()
                else:
                    return False
            # if it is an opening:
            else:
                stack.append(char)
        # return true if stack is empty; if not stack
        # return false if it is not empty: else False
        return True if not stack else False
                    