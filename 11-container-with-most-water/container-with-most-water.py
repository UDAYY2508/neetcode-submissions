class Solution:
    def maxArea(self, height: List[int]) -> int:
        

        l = 0
        r = len(height)-1
        maxCap=0
        while l<r:
            if height[l]>=height[r]:
                cap=(r-l) * min(height[l],height[r])
                r-=1

            elif height[r]>=height[l]:
                cap=(r-l) * min(height[l],height[r])
                l+=1
           
            maxCap=max(maxCap,cap)
            

        return maxCap
            
