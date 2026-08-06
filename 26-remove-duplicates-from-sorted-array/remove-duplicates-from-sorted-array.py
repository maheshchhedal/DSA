class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        first=0
        for i in range(1,n):
            if nums[i] != nums[first]:
                first+=1
                nums[first]=nums[i]
        return first+1

        
        

        