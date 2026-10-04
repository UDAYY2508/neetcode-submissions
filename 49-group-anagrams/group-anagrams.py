class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        res = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            res[key].append(word)

        return list(res.values())