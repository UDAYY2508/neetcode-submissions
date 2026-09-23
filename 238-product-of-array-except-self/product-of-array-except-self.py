class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n1 = [1] + nums
        n2 = nums + [1]
        i=1
        while i < len(n1):
            n1[i]=n1[i]*n1[i-1]
            i+=1
        j=len(n2)-2
        while j >= 0:
            n2[j]=n2[j]*n2[j+1]
            j-=1
        n1.pop()
        n2.pop(0)

        for i in range(len(nums)):
            nums[i]=n1[i]*n2[i]

        return nums
