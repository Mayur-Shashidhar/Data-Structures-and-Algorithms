class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()

        result = []
        permutation = []
        visited = [False] * len(nums)

        def backtrack():
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue

                permutation.append(nums[i])
                visited[i] = True

                backtrack()

                permutation.pop()
                visited[i] = False

        backtrack()

        return result
