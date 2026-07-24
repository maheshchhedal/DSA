class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = n
        product=1
        sum=0
        while  temp>0:
            r=temp%10
            product= product * r
            sum= sum + r
            result= product- sum
            temp//=10
        return result
