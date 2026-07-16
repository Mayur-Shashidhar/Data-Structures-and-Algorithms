class Solution(object):
    def permute(self, nums):
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
                
                permutation.append(nums[i])
                visited[i] = True

                backtrack()

                permutation.pop()
                visited[i] = False
        
        backtrack()

        return result
