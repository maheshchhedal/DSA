class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        ans=0
        for answer in accounts:
            ans=max(ans,sum(answer))
        return ans