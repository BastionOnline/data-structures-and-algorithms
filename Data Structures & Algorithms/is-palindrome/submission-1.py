class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            leftPointer = s[l].lower()
            rightPointer = s[r].lower()
            
            while l < r and not self.alphaNum(leftPointer):
                l += 1
            while r > l and not self.alphaNum(rightPointer):
                r -= 1

            if leftPointer != rightPointer:
                return False

            l, r = l +1, r-1

        return True

    def alphaNum(self, c):
        return (ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
            