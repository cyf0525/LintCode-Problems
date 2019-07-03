class Solution:
    """
    @param nums: List[List[int]]
    @param r: an integer
    @param c: an integer
    @return: return List[List[int]]
    """

    def matrixReshape(self, nums, r, c):
        # write your code here
        row = len(nums)
        col = len(nums[0])

        if row * col != r * c:
            return nums


        else:
            temp = []
            for i in range(len(nums)):
                temp += nums[i]

            res = []

            for j in range(r):
                res.append(temp[c * j:c * j + c])
            return res
