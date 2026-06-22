class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        answer = [-1] * n
        stack = []

        for i in range(2 * n):
            curr = nums[i % n]
            while stack and curr > nums[stack[-1]]:
                idx = stack.pop()
                answer[idx] = curr
            if i < n:
                stack.append(i)

        return answer
