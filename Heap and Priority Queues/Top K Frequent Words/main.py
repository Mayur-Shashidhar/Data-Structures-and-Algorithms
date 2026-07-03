class Pair:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq


class Solution(object):
    def topKFrequent(self, words, k):
        count = Counter(words)
        heap = []

        for word, freq in count.items():
            heapq.heappush(heap, Pair(word, freq))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        while heap:
            result.append(heapq.heappop(heap).word)

        return result[::-1]
