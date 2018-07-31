class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            temp = target-nums[i]
            if temp in nums[i+1:]:
                nums_temp=nums[i+1:].index(temp)
                return [i,nums_temp+i+1]
