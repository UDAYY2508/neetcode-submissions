class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        cou =0
        for num in hours:
            if num >= target:
                cou+=1
        return cou