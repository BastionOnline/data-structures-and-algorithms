class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSet = set(nums)
        print(numsSet)
    
        i = target - nums[0]

        print(nums)
        j = nums.index(i)
        if j == 0:
            nums.pop(0)
            j = nums.index(i)+1

        return [0, j]
