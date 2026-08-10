class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        heap = []

        for i in nums:
            count[i] = count.get(i,0) + 1

        for n , f in count.items():
            heapq.heappush(heap,(f,n))
            if len(heap) > k:
                heapq.heappop(heap)
        return [n for f,n in heap]