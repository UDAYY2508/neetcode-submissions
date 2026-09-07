class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        count = 0
        for passenger in details:
            age = ""
            for i in range(len(passenger)-3,-1,-1):
                if passenger[i] == "M" or passenger[i] == "F" or passenger[i] == "O":
                    break 
                age += passenger[i]
                if int(age[::-1]) > 60:
                    count+=1
        return count 