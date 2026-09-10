class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # initiate left and right
        l, r = 0, len(numbers)-1

        # use while loop to eval checksum
        while l<r:
            checkSum = numbers[l]+numbers[r]
        # if checksum is more than target move left
            if checkSum > target:
                r -=1
        # if checksum is less than target, move right
            elif checkSum < target:
                l +=1
        # if checksum == target, return +1 indexes
            else:
                return [l+1, r+1]
        
        return []