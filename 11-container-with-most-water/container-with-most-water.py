class Solution:
    def maxArea(self, height: list[int]) -> int:
        
        l = 0
        r = len(height)-1

        maxx = 0 

        while l<r:
            if height[l]<=height[r]:
                vol = (r-l) * min(height[l],height[r])
                maxx = max(maxx,vol)
                l+=1
            else: 
                vol = (r-l) * min(height[l],height[r])
                maxx = max(maxx,vol)
                r-=1
        return maxx