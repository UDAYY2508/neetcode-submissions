class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult = 1
        r_mult = 1

        l = []
        r = []
        res = []

        for i in range(len(nums)):
            l.append(l_mult)
            l_mult *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            r.append(r_mult)
            r_mult *= nums[i]
        r = r[::-1]

        for i in range(len(nums)):
            res.append(l[i] * r[i])

        return res