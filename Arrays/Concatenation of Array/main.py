class Solution(object):
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0] * 2 * n
        ans = nums + nums
        return ans
