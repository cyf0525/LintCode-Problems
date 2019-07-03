
class Solution:
    """
    @param  : An integer
    @param  : An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self,k,n):
        result = 0
        for i in range(0,n+1):
            result+=str(i).count(str(k))
        return result
