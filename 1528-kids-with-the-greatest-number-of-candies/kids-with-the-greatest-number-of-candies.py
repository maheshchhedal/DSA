class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        arr=[]
        maximum=max(candies)
        for i in candies:
            if i + extraCandies>= maximum:
                arr.append(True)
            else:
                arr.append(False)
                
        return arr
        