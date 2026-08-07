class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.split()
        last_index= len(s)-1
        return len(s[last_index])
        