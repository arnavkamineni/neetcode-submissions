class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 1
        for num in nums:
            thisLen = 1
            if num-1 not in numSet:
                next = num + 1
                while next in numSet:
                    thisLen += 1
                    next += 1
            maxLen = max(maxLen, thisLen)
        if len(nums) == 0:
            return 0
        return maxLen        