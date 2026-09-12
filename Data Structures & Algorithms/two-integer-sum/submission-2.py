class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsSet = set(nums)
    
        i = target - nums[0]
        print(i)

        j = nums.index(i)
        return [0, j]
