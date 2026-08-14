class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        strs = s + t
        dict1 = {}

        for i in strs:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i] = dict1[i] + 1

        for key, val in dict1.items():
            if val % 2 != 0:
                return key

     


            
        