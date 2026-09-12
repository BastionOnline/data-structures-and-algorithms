class Solution:
    def isValid(self, s: str) -> bool:
        # create 2 hashes
        # divide symbol by 10, let that be key and modulo be value
        rightHash = {4:1, 9:3, 12:5}
        leftHash = {4:0, 9:1, 12:3}
            # one with open symbols
            # one with close symbols
        
        l = 0
        # initiate 2 pointers, one at start, other at end of string
        for r in range(len(s),0,1):
            while l < r:
                # let the left check the left hash, let the right check the right hash
                leftKey = (s[l]/10)
                rightKey = (s[r]/10)
                if (leftKey == righKey and
                    leftHash[leftKey] == s[l]%10 and
                    rightHash[rightKey] == s[r]%10):
                    l +=1
                else:
                    return False
        return True

                    
