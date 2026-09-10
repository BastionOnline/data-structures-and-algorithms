class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # need to choose from value inside piles, cant have a pile with nothing
            # so no 0
        l, r = 1, max(piles)
        res = r

        while l <= r:
            timeElapsed = 0
            m = l + (r-l)//2

            # go through each pileee how much time it takes
            for pile in piles:
                timeElapsed += math.ceil(pile/m)

            if timeElapsed <= h:
                res = min(res,m)
                r = m-1
            else:
                # dont update result because we went over
                l = m+1
        return res