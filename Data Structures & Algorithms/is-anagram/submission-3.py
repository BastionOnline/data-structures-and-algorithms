class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charsAr = []

        for i in s:
            charsAr.append(i)

        for i in t:
            if i in charsAr:
                print(i)
                charsAr.remove(i)
            else:
                return False

        print(charsAr)
        print(len(charsAr) == 0)

        if len(charsAr) != 0:
            return False
        else:
            return True
