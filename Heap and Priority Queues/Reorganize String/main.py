class Solution(object):
    def reorganizeString(self, s):
        count = Counter(s)
        maxHeap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(maxHeap)
        prevFreq, prevChar = 0, ""
        result = []

        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            result.append(char)
            freq += 1

            if prevFreq < 0:
                heapq.heappush(maxHeap, (prevFreq, prevChar))

            prevFreq, prevChar = freq, char

        if len(result) != len(s):
            return ""

        return "".join(result)
