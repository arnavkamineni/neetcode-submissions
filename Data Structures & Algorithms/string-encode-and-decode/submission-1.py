class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for val in strs:
            out += val + "~"
        return out

    def decode(self, s: str) -> List[str]:
        start = 0
        out = []
        for i in range(len(s)):
            if s[i] == "~":
                out.append(s[start:i])
                start = i+1
        return out
