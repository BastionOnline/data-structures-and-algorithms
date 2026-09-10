class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for index1, val in enumerate(nums):
            diff = target - val

            if diff in prevMap:
                return [prevMap[diff], index1]
            prevMap[val] = index1