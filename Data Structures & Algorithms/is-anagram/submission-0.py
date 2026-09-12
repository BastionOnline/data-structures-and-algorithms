class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        charsAr = []

        for i in s:
            charsAr.append(i)

        for i in t:
            if i in charsAr:
                charsAr.remove(i)

        if len(chars) == 0 and len(charsAr) == 0:
            return True
        else:
            return False
