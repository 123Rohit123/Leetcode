class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(ransomNote) > len(magazine):
            return False
        hashMap = {}
        for character in range(len(magazine)):
            if magazine[character] not in hashMap:
                hashMap[magazine[character]] = 1
            else:
                hashMap[magazine[character]] += 1
        for member in range (len(ransomNote)):
            if ransomNote[member] not in hashMap:
                return False
            elif hashMap[ransomNote[member]] == 0:
                return False
            else:
                hashMap[ransomNote[member]] -= 1  
        return True
        