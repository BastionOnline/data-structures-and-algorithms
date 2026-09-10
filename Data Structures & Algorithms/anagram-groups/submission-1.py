class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # unique occurances of letters will form unique anagram key
        res = defaultdict(list)
        
        # go one word at a time
        for string in strs:
            
            # create an array of 26 0's that will be incremented as count is done
            count = [0] * 26

            # go through each letter in the word
            for char in string:

                # go to the letter index based on the ascii value
                # increment by 1
                count[ord(char) - ord('a')] +=1

            # count, mutable, can be changed. not good to use as key
            # [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]

            # tuple(count), immutable tuple, cannot be changed. good to use as key.
            # (1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)

            # res[key]
            # look up key and add the word being assessed. 
            res[tuple(count)].append(string)
        
        # return the values
        return list(res.values())
                

            
        
