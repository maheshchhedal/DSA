class Solution(object):
    def twoSum(self, nums, target):
        # n=len(nums)
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         if nums[i]+ nums[j]==target:
        #             return [i,j]
        # return []

        #using dictionary
        n=len(nums)
        freq={}
        for i in range(n):
            rem=target-nums[i]
            if rem in freq:
                return [freq[rem],i]
            else:
                freq[nums[i]]=i
                
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        