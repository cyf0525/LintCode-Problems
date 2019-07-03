class Solution:
    """
    @param n: an integer
    @return: if n is a power of two
    """

    def isPowerOfTwo(self, n):
        # Write your code here
        if n == 1:
            return True

        while n % 2 == 0:
            n = n / 2
            if n == 2 or n == 1:
                return True
        else:
            return False
