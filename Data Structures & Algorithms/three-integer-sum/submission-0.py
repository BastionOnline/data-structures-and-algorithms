class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # array to return
        res = []
        # sort input
        nums.sort()

        # make it a 2 sum problem
        # why enum?
        for i, a in enumerate(nums):
            if a > 0:
                break

            #
            if i > 0 and a == nums[i-1]:
                continue

            # 2 sum solution
            l, r = i + 1, len(nums)-1
            
            while l < r:
                checkSum = a + nums[l] + nums[r]
                if checkSum > 0:
                    r -= 1
                elif checkSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # explain this piece
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res

