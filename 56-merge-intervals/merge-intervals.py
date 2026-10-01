class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
            intervals.sort()
            merge = [intervals[0]]
            for i in intervals:
                last =merge[-1]
    
                if last[-1]>=i[0]:
                    last[-1]=max(last[-1],i[1])
                else:
                    merge.append(i)
            return merge
