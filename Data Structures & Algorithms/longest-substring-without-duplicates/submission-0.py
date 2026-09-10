class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maxlength
        longestSubstring = 0 
        # hashset
        substring = set()

        l = 0

        # right pointer goes through every char
        # Returns INDEX
        for r in range(len(s)):

            # get to duplicate, update window and set
                # get value USING THE INDEX r s[r]
            while s[r] in substring:
                # remove VALUE on the LEFT
                substring.remove(s[l])
                
                # move pointer up 1
                l +=1

            substring.add(s[r])

            # better to check length of window manual check incase DS change
            longestSubstring = max(longestSubstring, r-l+1)
        
        return longestSubstring