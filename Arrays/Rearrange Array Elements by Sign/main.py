class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        answer = [0] * n
        pos = 0
        neg = 1

        for num in nums:
            if num > 0:
                answer[pos] = num
                pos += 2
            else:
                answer[neg] = num
                neg += 2

        return answer
