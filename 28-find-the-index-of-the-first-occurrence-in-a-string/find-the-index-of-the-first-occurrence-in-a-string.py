class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            j = 0
            while j < len(needle):
                if i + j >= len(haystack) :
                    break
                if haystack[i + j] != needle[j]:
                    break
                j += 1
                if j == len(needle):
                    return i
        return -1
    