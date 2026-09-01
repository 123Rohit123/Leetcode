class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        freq = {}

        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        for j in t:
            if j in freq:
                freq[j] -= 1
            else:
                return False
        
        for value in freq.values():
            if value != 0:
                return False

        return True