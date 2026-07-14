class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        combination = []

        def backtrack(index, target):
            if target == 0:
                result.append(combination[:])
                return

            if target < 0:
                return
            
            for i in range(index, len(candidates)):
                combination.append(candidates[i])
                backtrack(i, target - candidates[i])
                combination.pop()
        
        backtrack(0, target)

        return result
