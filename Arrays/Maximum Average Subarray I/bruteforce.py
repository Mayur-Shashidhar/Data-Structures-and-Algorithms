class Solution(object):
    def findMaxAverage(self, nums, k):
        max_avg = float('-inf')

        for i in range(len(nums) - k + 1):
            current_sum = 0

            for j in range(i, i + k):
                current_sum += nums[j]

            current_avg = current_sum / float(k)
            max_avg = max(max_avg, current_avg)

        return max_avg
