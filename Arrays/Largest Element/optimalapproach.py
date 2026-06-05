class Solution(object):
  def largestElement(self, nums):
    largest = nums[0]

    for i in range(1,n):
      if largest < nums[i]:
        largest = nums[i]

    return largest
