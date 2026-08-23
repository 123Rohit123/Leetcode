class Solution(object):
    def twoSum(self, nums, target):
        dict_num = {}
        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in dict_num:
                return(dict_num[compliment],i)

            dict_num[nums[i]] = i

        return []