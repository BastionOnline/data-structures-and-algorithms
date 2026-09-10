class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        single = set()

        for num in nums:
            if num in single:
                return True
            else:
                single.add(num)
        return False