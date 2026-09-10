class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        while nums:
            num = nums.pop()
            if num in nums:
                return True
        return False