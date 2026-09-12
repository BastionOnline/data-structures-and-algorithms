class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arrayLength = len(nums)
        leftArray = []
        rightArray = []
        # sumArray = []

        i = 0
        runningProduct = 1
        while i < arrayLength:
            if i == 0:
                leftArray.append(1)
                i +=1
            else:
                runningProduct *= nums[i-1]
                leftArray.append(runningProduct)
                i +=1
        
        i = arrayLength
        runningProduct = 1
        while i > 0:
            if i == arrayLength:
                rightArray.append(1)
                i -=1
            else:
                runningProduct *= nums[i]
                rightArray.insert(0,runningProduct)
                i -=1

        sumArray = [x * y for x,y in zip(leftArray, rightArray)]
        return sumArray