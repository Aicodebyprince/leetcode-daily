class Solution(object):
    def moveZeroes(self, nums):
        k = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                if i != k:
                    nums[i] = 0
                k += 1
