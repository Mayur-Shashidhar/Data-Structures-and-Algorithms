class Solution(object):
    def combinationSum3(self, k, n):
        result = []
        combination = []

        def backtrack(start, target):
            if len(combination) == k:
                if target == 0:
                    result.append(combination[:])
                return
            
            if target < 0:
                return
            
            for i in range(start, 10):
                combination.append(i)
                backtrack(i + 1, target - i)
                combination.pop()
        
        backtrack(1, n)

        return result
