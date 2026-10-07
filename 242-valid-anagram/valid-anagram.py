class Solution(object):
    def isAnagram(self,s,t):
        if len(s) != len(t):
            return False
        freq = {}
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]] += 1
        for j in range(len(t)):
            if t[j] in freq:
                freq[t[j]] -= 1
            else:
                return False
        for value in freq.values():
            if value != 0:
                return False
        return True