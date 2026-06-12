class Solution(object):
    def intersection(self, nums1, nums2):
        nums1_set = set(nums1)
        answer = set()

        for num in nums2:
            if num in nums1_set:
                answer.add(num)

        return list(answer)
