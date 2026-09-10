class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1

        # go through l one at a time
        while l <= r:
            # setup middle pointer
                # cant use len(nums) because this is FIXED
                # / float rounding
                # // rounds down, to neg inifity
            # can have integer overflow using: m = (l+r)//2
            # get the distance between them first
            m = l+((r-l)//2)
            

            if target < nums[m]:
                r = m-1
            elif target > nums[m]:
                l = m+1
            else:
                return m
        return -1
                

