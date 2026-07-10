class Solution(object):
    def findClosestElements(self, arr, k, x):
        heap = []

        for num in arr:
            distance = abs(num - x)
            heapq.heappush(heap, (-distance, -num))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        
        while heap:
            result.append(-heapq.heappop(heap)[1])

        result.sort()

        return result
