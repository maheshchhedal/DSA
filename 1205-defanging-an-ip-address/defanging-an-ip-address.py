class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        # return address.replace('.','[.]')
        ans=''
        for i in address:
            if i !='.':
                ans +=i
            else:
                ans +='[.]'
        return ans