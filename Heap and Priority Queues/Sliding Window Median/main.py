class Solution(object):
    def medianSlidingWindow(self, nums, k):
        small = []   # Max Heap (store negatives)
        large = []   # Min Heap
        delayed = defaultdict(int)

        smallSize = 0
        largeSize = 0

        def prune(heap):
            while heap:
                num = -heap[0] if heap is small else heap[0]
                if delayed[num]:
                    delayed[num] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def balance():
            nonlocal smallSize, largeSize

            if smallSize > largeSize + 1:
                heapq.heappush(large, -heapq.heappop(small))
                smallSize -= 1
                largeSize += 1
                prune(small)

            elif smallSize < largeSize:
                heapq.heappush(small, -heapq.heappop(large))
                smallSize += 1
                largeSize -= 1
                prune(large)

        def addNum(num):
            nonlocal smallSize, largeSize

            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                smallSize += 1
            else:
                heapq.heappush(large, num)
                largeSize += 1

            balance()

        def removeNum(num):
            nonlocal smallSize, largeSize

            delayed[num] += 1

            if num <= -small[0]:
                smallSize -= 1
                if num == -small[0]:
                    prune(small)
            else:
                largeSize -= 1
                if large and num == large[0]:
                    prune(large)

            balance()

        def median():
            if k % 2:
                return float(-small[0])
            return (-small[0] + large[0]) / 2.0

        for i in range(k):
            addNum(nums[i])

        result = [median()]

        for i in range(k, len(nums)):
            addNum(nums[i])
            removeNum(nums[i - k])
            result.append(median())

        return result
