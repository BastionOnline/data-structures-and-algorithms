class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # start both at the beginning
        slow, fast = 0, 0

        # init pointers
        # treat array like linked list
        # use value stored at index as address for next index
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                # slow and fast now share common idx
                break
        
        # init another slow pointer from start again
        slow2 = 0

        # move each node by one now
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                # both pointers have now met the cycle entrance
                break
        
        # return one of them
        return slow2