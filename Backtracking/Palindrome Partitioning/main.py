class Solution(object):
    def partition(self, s):
        result = []
        partition = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start):
            if start == len(s):
                result.append(partition[:])
                return

            for end in range(start, len(s)):
                if isPalindrome(start, end):
                    partition.append(s[start:end + 1])
                    backtrack(end + 1)
                    partition.pop()

        backtrack(0)
        return result
