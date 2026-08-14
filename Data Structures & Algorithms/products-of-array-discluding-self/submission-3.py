class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
            l = [] 
            r = []
            l_mul = 1
            r_mul = 1
            res = []

            for i in range(len(nums)):
                l.append(l_mul)
                l_mul *= nums[i]
            for i in range(len(nums) -1,-1,-1):
                r.append(r_mul)
                r_mul *= nums[i]
            r = r[::-1]

            for i in range(len(nums)):
                res.append(l[i] * r[i])

            return res
