class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        workers = []

        for q, w in zip(quality, wage):
            workers.append((float(w) / q, q))
        workers.sort()

        heap = []
        qualitySum = 0
        result = float('inf')

        for ratio, q in workers:
            heapq.heappush(heap, -q)
            qualitySum += q

            if len(heap) > k:
                qualitySum += heapq.heappop(heap)

            if len(heap) == k:
                result = min(result, ratio * qualitySum)

        return result
