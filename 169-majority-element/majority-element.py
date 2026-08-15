class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1={}
        n=len(nums)
        maxs=0
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]=dict1[i]+1

        for key, value in dict1.items():
            if value > n / 2:
                return key
        