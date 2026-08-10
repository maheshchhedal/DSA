class Solution(object):
    def sotrString(self,s):
        s1= list(s)
        s1.sort()
        return ''.join(s1)
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict1={}
        for s in strs:
            key=self.sotrString(s)
            if key  in dict1:
                dict1[key].append(s)
            else:
                dict1[key]=[s]
        return list(dict1.values())


            
           
        