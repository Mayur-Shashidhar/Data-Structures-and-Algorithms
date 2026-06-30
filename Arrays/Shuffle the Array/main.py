class Solution(object):
    def shuffle(self, nums, n):
        result = []
        l1 = nums[:n]
        l2 = nums[n:]

        for i in range(n):
            result.append(l1[i])
            result.append(l2[i])
        
        return result
