class Solution(object):
    def isSubsequence(self, s, t):
        if s == '': return True
        if len(s) > len(t) : return False

        i = 0
        for j in range(len(t)):
            if t[j] == s[i]:
                if i == len(s)-1:
                    return True
                else:
                    i += 1
        return False