class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        for word in strs:
            countDict = self.counter(word)
            key = tuple(sorted(countDict.items()))
            if key in out:
                out[key].append(word)
            else:
                out[key] = [word]
        # print(out)
        return list(out.values())

    def counter(self, word):
        counts = {}
        for char in range(0, len(word)):
            if word[char] in counts:
                counts[word[char]] += 1
            else:
                counts[word[char]] = 1
        # print(counts)
        return counts
        