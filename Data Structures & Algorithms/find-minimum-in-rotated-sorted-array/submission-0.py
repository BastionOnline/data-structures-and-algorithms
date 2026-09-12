class Solution:
    def findMin(self, nums: List[int]) -> int:
        # create leftindex,rightindex pointer
        leftIdx, rightIdx = 0, len(nums)-1

        # while left < right, dont want infinite loop
        while leftIdx < rightIdx:
            # create midIdx
            midIdx = leftIdx + (rightIdx -leftIdx)//2
            # if midIdx > rightIdx:
            if nums[midIdx] > rightIdx:
                # left = midIdx+1
                leftIdx = midIdx+1
            # else:
            else:
                # right = midIdx+1
                rightIdx = midIdx-1
        # return midIdx
        return midIdx