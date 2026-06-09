class Solution(object):
    def sortColors(self, nums):
        count_zero = 0
        count_one = 0
        count_two = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count_zero += 1
            elif nums[i] == 1:
                count_one += 1
            else:
                count_two += 1

        index = 0

        for i in range(count_zero):
            nums[index] = 0
            index += 1

        for i in range(count_one):
            nums[index] = 1
            index += 1

        for i in range(count_two):
            nums[index] = 2
            index += 1
