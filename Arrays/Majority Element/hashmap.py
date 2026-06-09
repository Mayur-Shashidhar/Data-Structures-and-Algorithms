class Solution(object):
    def majorityElement(self, nums):
        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        for key, value in hashmap.items():
            if value > len(nums) // 2:
                return key
