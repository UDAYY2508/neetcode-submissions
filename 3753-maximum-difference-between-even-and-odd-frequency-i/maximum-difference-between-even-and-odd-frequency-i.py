class Solution:
    def maxDifference(self, s: str) -> int:
          
        maximum = 0
        minEven = float("inf")
        maxOdd = 0
        mp = {}

        for i in range(len(s)):
            mp[s[i]] = mp.get(s[i],0)+1
        
        for key,frq in mp.items():
            even = 0
            odd = 0
            if frq%2 == 0:
                even = frq
                minEven = min(minEven,even)
                
            else:
                odd = frq
                maxOdd = max(maxOdd,odd)

        maximum = maxOdd - minEven

        return maximum  