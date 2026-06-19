class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []

        p_count = {}
        window_count = {}

        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1

        for i in range(len(p)):
            window_count[s[i]] = window_count.get(s[i], 0) + 1

        result = []

        if window_count == p_count:
            result.append(0)

        left = 0

        for right in range(len(p), len(s)):
            window_count[s[right]] = window_count.get(s[right], 0) + 1
            window_count[s[left]] -= 1
            if window_count[s[left]] == 0:
                del window_count[s[left]]
            left += 1
            if window_count == p_count:
                result.append(left)

        return result
