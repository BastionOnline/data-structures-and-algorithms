class Solution:

    def encode(self, strs: List[str]) -> str:
        
        merge = ''

        for string in strs:
            total = 0
            compWord = ''

            for char in string:
                total +=1
                compWord += char
                # print(compWord)
            merge = f'{merge}{total}#{compWord}'
            # print(merge)

        return merge

            
        
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        orgArray = []
        pointer1 = 0
        pointer2 = 0

        # print(s)
        i = 0 

        while i < len(s):
            # create scout
            j = i
            
            while s[j] != "#":
                # if char != "#":
                j+=1
                if s[j] == "#":
                    # print(f's: {s}')
                    # print(f'i: {i}')
                    # print(f'key:{key}')
                    # print(value)
                    # print(f'char: {s[i]}')
                    # print(f'number slice: {s[i:j]}')
                    length = int(s[i:j])
                    # length = int(s[pointer2:key])
                    # print(length)
                    pointer1 = j+1
                    # print(f'pointer1: {pointer1}')
                    pointer2 = pointer1+length
                    word = s[pointer1:pointer2]
                    orgArray.append(word)
                    # print(orgArray)
                    # s = s[pointer2:]
                    i = pointer2
                    # print(i)
        return orgArray    

            