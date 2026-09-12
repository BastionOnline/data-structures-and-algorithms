class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # let individual values increment their keys
        count = defaultdict()
        minK = []
        
        # go one item at a time
        for item in nums:
            if item not in count:
                count[item] = count.get(item, 0) +1
            else:
                count[item] += 1

        print(count)


        for item in count:
            if count[item] >=k:
                minK.append(item)

        print(count)
        print(minK)
        return minK