import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        heap = []

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0)+1
        
        for num,frq in count.items():
            heapq.heappush(heap,(frq,num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for frq,num in heap]
            

        
