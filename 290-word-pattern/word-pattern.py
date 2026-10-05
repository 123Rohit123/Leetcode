class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False
        h1 = {}
        h2 = {}
        for char1, word1 in zip(pattern, words):
            if (char1 in h1 and h1[char1] != word1) or (word1 in h2 and h2[word1] != char1):
                return False
            h1[char1] = word1
            h2[word1] = char1
        return True
        