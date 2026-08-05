class Solution(object):
    def runningSum(self, nums):
        sum=0
        lists=[]
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in nums:
            sum= sum + i
            lists.append(sum)
        return lists


        