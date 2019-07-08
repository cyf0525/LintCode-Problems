


class Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """
    def __init__(self,nums,k):
        self.nums = nums
        self.k = k


    def sameNumber(self):
        # Write your code here
        d = {}

        for i, n in enumerate(self.nums):
            if n in d:
                # check
                if i - d[n][-1] < self.k:
                    return "YES"
            else:
                d[n] = [i]
                print d[n]

        return "NO"




