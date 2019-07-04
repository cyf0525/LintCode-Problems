class Solution:
    """
    @param num: a positive integer
    @return: if num is a perfect square else False
    """
    def isPerfectSquare(self, num):
        # write your code here
        if (num**0.5)%1 == 0:
            return True
        else:
            return False
