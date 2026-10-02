class Solution(object):
    def isIsomorphic(self, s, t):
        h1 = {}
        h2 = {}

        for char1, char2 in zip(s,t):
            if (char1 in h1 and h1[char1] != char2) or (char2 in h2 and h2[char2] != char1):
                return False
            h1[char1] = char2
            h2[char2] = char1
        return True
