class Solution:

    def encode(self, strs: List[str]) -> str:
        
        merge = ''

        for string in strs:
            total = 0
            compWord = ''

            for char in string:
                total +=1
                compWord += char
            merge = f'{merge}{total}#{compWord}'
        return merge

            
        
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        orgArray = []
        pointer1 = 0
        pointer2 = 0

        while len(s) > 0:
            pointer1 = 2
            pointer2 = int(s[0])+2

            word = s[pointer1:pointer2]
            orgArray.append(word)

            s = s[pointer2:]
        return orgArray


        

