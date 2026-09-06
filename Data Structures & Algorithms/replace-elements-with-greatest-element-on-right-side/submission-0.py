class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = 0

        
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                maxx = max(maxx,arr[j])
            arr[i] = maxx
            maxx = 0
        arr[-1] = -1
        return arr