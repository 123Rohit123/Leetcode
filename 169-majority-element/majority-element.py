class Solution(object):
    def majorityElement(self, nums):
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for i in nums:
            if freq[i] > len(nums) // 2:
                return i      