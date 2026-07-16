class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()

        result = []
        combination = []

        def backtrack(index, target):
            if target == 0:
                result.append(combination[:])
                return

            if target < 0:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                combination.append(candidates[i])
                backtrack(i + 1, target - candidates[i])
                combination.pop()

        backtrack(0, target)

        return result
