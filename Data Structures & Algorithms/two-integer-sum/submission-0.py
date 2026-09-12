class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sort
        nums.sort()

        # numsSet = set(nums)
        start = target - nums[0]
        # try first number
        if start < 0:
            print(True)
            start = abs(start)
        
        print(start)
        # if negative, subtract
        # find that smallest whole number
        