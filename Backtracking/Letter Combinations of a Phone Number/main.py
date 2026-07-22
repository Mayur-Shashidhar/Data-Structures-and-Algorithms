class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        combination = []

        def backtrack(index):
            if index == len(digits):
                result.append("".join(combination))
                return
            
            letters = phone[digits[index]]

            for letter in letters:
                combination.append(letter)
                backtrack(index + 1)
                combination.pop()
        
        backtrack(0)

        return result
