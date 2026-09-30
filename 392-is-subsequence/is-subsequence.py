class Solution(object):
    def isSubsequence(self,s,t):
        if s == '': return True
        if len(s) > len(t) : return False

        pointer1 = 0
        for pointer2 in range(len(t)):
            if t[pointer2]== s[pointer1]:
                if pointer1 == len(s)-1:
                    return True
                else:
                    pointer1 += 1
        return False