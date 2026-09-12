class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        core = {}

        chars = {}
        anagrams = []

        # take the word
        for string in strs:
            # this is the temp comparison holder
            temp = {}
            # go through each letter in the word
            for char in string:
                # if the letter is not in the core, add it to temp
                if char not in core:
                    temp[char] = temp.get(char, 0) +1
                    print(temp)
            if char not in chars or chars[char] == 0:
                print(False)
                return False
                

            
        
