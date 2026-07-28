class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 0
        
        pairs = list(freqs.items())
        pairs.sort(key=lambda x: x[1], reverse = True)
        print(pairs)
        outPairs = pairs[0: k]
        outList = []
        for pair in outPairs:
            outList.append(pair[0])
        return outList       
        
        