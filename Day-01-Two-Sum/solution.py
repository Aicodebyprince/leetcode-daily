class Solution:
    def twoSum(self, nums, target):
        data = {}

        for i in range(len(nums)):
            need = target - nums[i]

            if need in data:
                return [data[need], i]

            data[nums[i]] = i
