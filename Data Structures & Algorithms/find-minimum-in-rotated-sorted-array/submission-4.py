class Solution:
    def findMin(self, nums: List[int]) -> int:
        # create leftindex,rightindex pointer
        leftIdx, rightIdx = 0, len(nums)-1

        # while left < right, dont want infinite loop
        while leftIdx < rightIdx:
            # create midIdx
            midIdx = leftIdx + (rightIdx -leftIdx)//2
            
            # if midIdx > rightIdx:
            # Condition: GREATER THAN ONLY
            # Mid is 100% NOT the minimum -> leftIdx = midIdx + 1
            if nums[midIdx] > nums[rightIdx]:
                # left = midIdx+1
                leftIdx = midIdx+1

            # Conditions: LESS THAN OR EQUAL TO
            # Mid COULD BE the minimum -> rightIdx = midIdx
            else:
                # right = midIdx+1
                rightIdx = midIdx
        # cannot return midIdx because it is a local variable
        # left acts as more of the runner, best to use this one.
        return nums[leftIdx]