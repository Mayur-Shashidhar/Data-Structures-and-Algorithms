class Solution(object):
    def leastInterval(self, tasks, n):
        count = Counter(tasks)
        maxHeap = [-freq for freq in count.values()]
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0

        while maxHeap or queue:
            time += 1
            if maxHeap:
                freq = 1 + heapq.heappop(maxHeap)
                if freq != 0:
                    queue.append((freq, time + n))
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time  
