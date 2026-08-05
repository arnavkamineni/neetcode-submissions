class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        freqs = set()
        ans = 0

        for r in range(len(s)):
            while s[r] in freqs:
                freqs.remove(s[l])
                l += 1

            freqs.add(s[r])
            ans = max(ans, r - l + 1)

        return ans

