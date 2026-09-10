class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # track current area max
        maxArea = 0
        # init left and right pointer
        l, r = 0, len(heights)-1
        
        # while l<r:
        while l<r:
            # figure out how to evaluate bars
            # length x width
            # (height of bars) x (distance between indexes)
            # area = min(h[l], h[r]) x (r-l)
                # needs to be min because at max, if the bars are not equal, it will spill at the min point
            currentArea = min(heights[l], heights[r]) * (r-l)
            maxArea = max(maxArea, currentArea)
            
            # if heig ht-left is less than height-right
            if heights[l] < heights[r]:
            # move height-left, 1 unit right
                l +=1

            # if height-right is less than height-left
            elif heights[l] > heights[r]:
            # move height right, 1 unit left
                r -=1

            # if height-left== height-right
            else:
            # move either
                r -=1
            # return 
        return maxArea