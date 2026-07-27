class Solution(object):
    def restoreIpAddresses(self, s):
        result = []
        path = []

        def isValid(segment):
            if len(segment) > 1 and segment[0] == '0':
                return False
            return int(segment) <= 255

        def backtrack(index):
            if len(path) == 4:
                if index == len(s):
                    result.append(".".join(path))
                return

            for length in range(1, 4):
                if index + length > len(s):
                    break

                segment = s[index:index + length]

                if isValid(segment):
                    path.append(segment)
                    backtrack(index + length)
                    path.pop()

        backtrack(0)
        return result
