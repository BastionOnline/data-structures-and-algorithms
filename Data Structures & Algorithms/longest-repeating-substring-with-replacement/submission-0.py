class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        # left pointer
        l=0

        # right pointer
        for r in range(len(s)):

            # for character at position r, increment count
            count[s[r]] = count.get(s[r], 0) + 1

            # check that current window is valid; can use either if OR while
                # length of window (r-l +1), subtract
                # count of most frequent character
                    # goes through hashmap
            # shows the number of replacements that have to be done
            # if replacements is greater than what is allowed
            while (r-l +1) - max(count.values()) > k:
                
                # remove the character at the left of the window from the hash
                count[s[l]] -=1
                
                # move the pointer to the next left index in the window
                l +=1

            # set the result to max, size of window
            res = max(res, r-l +1)
        return res