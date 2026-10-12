class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                seen.remove(nums[L])
                L += 1
            if nums[R] in seen:
                return True
            seen.add(nums[R])
        return False