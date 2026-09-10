class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestLength = 0

        # go through each number
        for num in numSet:
            
            # check if num is start of sequence
            # if there is a left value, this is probably a mid/end element, skip it
            # if an earlier value does not exist, it is the start of a sequence
            if (num-1) not in numSet:
                
                # start counting
                length = 1
                
                # earlier understanding: if the next number is there
                # new understanding: AS LONG AS consecutive numbers appear
                    # better to use while to check ALL continuous numbers
                    # if only checks one
                while (num + length) in numSet:
                    
                    # increment count
                    length +=1

                # compare the longestLength found and updated if needed
                longestLength = max(length, longestLength)
            
        # after your done checking each number, return longest length
        return longestLength
