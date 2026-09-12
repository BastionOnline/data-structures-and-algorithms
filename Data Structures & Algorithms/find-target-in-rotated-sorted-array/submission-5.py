class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # set up beginning and end bound
        beg, end = 0, len(nums)-1

        # want to keep searching until
        # beginning and end converge at same idx
        while beg < end:
            mid = beg + (end - beg)//2

            # if target is right at middle
            if nums[mid] == target:
                return mid

            # check beginning sorted bound
            if nums[beg] <= nums[mid]:
                # if the target is within this bound at all
                if nums[beg] <= target <= nums[mid]:
                    end = mid -1
                # if target is beyond this bound
                else:
                    beg = mid+1
            else:
                if nums[mid] <= target <= nums[end]:
                    beg = mid + 1
                else:
                    end = mid -1 
        return -1 if nums[beg] != target else end
            