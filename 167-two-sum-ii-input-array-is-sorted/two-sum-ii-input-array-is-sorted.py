class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        first=0
        second=len(numbers)-1

        while first <second:
            result=numbers[first]+ numbers[second]
            if result==target:
                return [first+1,second+1]
            elif result >target:
                second -=1
            else:
                first+=1

        
        