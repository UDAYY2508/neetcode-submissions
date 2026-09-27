class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        max_len=0
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i] and arr[i+1]<arr[i]:
                l=i
                r=i
                while l>0 and arr[l]>arr[l-1]:
                    l-=1
                while r<len(arr)-1 and arr[r]>arr[r+1]:
                    r+=1
                max_len=max(r-l+1,max_len)

        return max_len