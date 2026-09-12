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
            print(merge)

        return merge

            
        
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        orgArray = []
        pointer1 = 0
        pointer2 = 0

        print(s)
        # while len(s) > 0:
        #     pointer1 = 2
            # print(pointer1)
            # set up manual loop to find uptil the # sign

        for key, value in enumerate(s):
            if value == "#":
                print(f'key:{key}')
                print(value)
                length = int(s[pointer2:key])
                print(length)
                pointer1 = key+1
                print(f'pointer{pointer1}')
                pointer2 = int(key)+1+length
                word = s[pointer1:pointer2]
                orgArray.append(word)
                print(orgArray)
        # return orgArra




            # pointer2 = int(s[0])+2
            # print(pointer2)

            # word = s[pointer1:pointer2]
            # print(f'word {word}')

            # orgArray.append(word)
            # print(f'org {orgArray}')

            # s = s[pointer2:]
            # print(s)
        return orgArray


        

