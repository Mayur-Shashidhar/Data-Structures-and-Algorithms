class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False
        char_to_word = {}
        word_to_char = {}

        for i in range(len(pattern)):
            if pattern[i] in char_to_word and char_to_word[pattern[i]] != words[i]:
                return False
            if words[i] in word_to_char and word_to_char[words[i]] != pattern[i]:
                return False
            char_to_word[pattern[i]] = words[i]
            word_to_char[words[i]] = pattern[i]

        return True
