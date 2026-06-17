class Solution(object):
    def largestNumber(self, nums):
        array = list(map(str, nums))
        array.sort(key = lambda x: x*10, reverse = True)

        if array[0] == "0":
            return "0"

        largest = ''.join(array)
        return largest
