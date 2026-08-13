class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        dict1={}
        n=len(nums)
        count=1

        dict1 = {}

        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = count
            else:
                dict1[nums[i]] =count+ 1

        for key, value in dict1.items():
            if value == 1:
                return key