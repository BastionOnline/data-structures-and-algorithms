class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        charsAr = []

        # for i, c in enumerate(s):
        #     chars[i] = c

        for i in s:
            charsAr.append(i)

        for i in t:
            if i in charsAr:
                print(i)
                charsAr.remove(i)

        print(chars)
        print(charsAr)
        print(len(chars) == 0)
        print(len(charsAr) == 0)

        if len(chars) == 0 and len(charsAr) == 0:
            return True
        else:
            return False
