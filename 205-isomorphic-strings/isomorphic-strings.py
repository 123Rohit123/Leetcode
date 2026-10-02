class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        h1 ={}
        h2 ={}
        for i,j in zip(s,t):
            if (i in h1 and h1[i] != j) or (j in h2 and h2[j] != i):
                return False
            h1[i] = j
            h2[j] = i
        return True            


