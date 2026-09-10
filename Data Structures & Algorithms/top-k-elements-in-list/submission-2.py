class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # create array of arrays
        # the INDEX of each array is used as the count for each item
        freq = [[] for i in range(len(nums) +1)]
        # print(freq)

        # count each value
        for n in nums:
            # see if the value exists in count
            # if not create it and then add one
            count[n] = count.get(n, 0) +1 

        for key, value in count.items():
            freq[value].append(key)

        res = []
        # iterates backwards: range(from the end, stop at the start, go one at a time)
        for i in range(len(freq)-1, 0, -1):
            # for each value with in each index
            for n in freq[i]:
                # add it to res
                res.append(n)
                # check if k has been met
                if len(res) == k:
                    return res
