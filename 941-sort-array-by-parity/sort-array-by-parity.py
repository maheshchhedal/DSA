class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        first = 0
        for i in range(n ):
            if nums[i]% 2==0:
                temp=nums[i]
                nums[i]=nums[first]
                nums[first]=temp
                first +=1
        return nums
        