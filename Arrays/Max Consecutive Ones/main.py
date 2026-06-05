class Solution(objects):
  def findMaxConsecutiveOnes(self, nums):
    current = 0
    maximum = 0

    for i in range(0,len(nums)):
      if nums[i] == 1:
        current += 1
        maximum = max(maximum, current)

      if nums[i] == 0:
        current = 0

    return max(current, maximum)
