class Solution(object):
    def firstUniqChar(self, s):
        freq= {}

        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        for j, i in enumerate(s):
            if freq[i] == 1:
                return j
        return -1
        