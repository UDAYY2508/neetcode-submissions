class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        bag_s = {}
        bag_t = {}

        for i in s:
            bag_s[i] = bag_s.get(i,0) + 1
        for j in t:
            bag_t[j] = bag_t.get(j,0) + 1

        return bag_s == bag_t
            