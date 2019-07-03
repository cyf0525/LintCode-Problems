class Solution:
    """
    @param num: a non-negative integer
    @return: one digit
    """

    def addDigits(self, num):
        # write your code here
        if num < 10:
            return num

        a = str(num)

        while len(str(a)) > 1:
            b = 0
            for i in range(len(a)):
                b += int(a[i])
            a = str(b)

        return b



