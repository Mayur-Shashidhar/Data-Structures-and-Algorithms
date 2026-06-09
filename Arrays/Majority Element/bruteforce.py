class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)

        for i in range(n):
            count = 0

            for j in range(n):
                if nums[j] == nums[i]:
                    count += 1

            if count > n // 2:
                return nums[i]
