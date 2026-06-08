class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        sum_of_n = (n*(n+1))/2
        sum_of_nums = 0
        for i in range(0, n):
            sum_of_nums += nums[i]
        
        missing = sum_of_n - sum_of_nums
        return missing
