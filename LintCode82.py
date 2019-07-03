class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        a = 0
        for i in A:
            if A.count(i) == 1:
                return i


