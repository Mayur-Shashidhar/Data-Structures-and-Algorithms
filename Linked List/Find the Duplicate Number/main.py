class Solution(object):
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        pointer = nums[0]

        while pointer != slow:
            pointer = nums[pointer]
            slow = nums[slow]

        return pointer
