class Solution:
    """
    @param nums: an integer array
    @return: the maximum product
    """
    def maximumProduct(self, nums):
        # Write your code here
        nums.sort()
        res1 = nums[-1]*nums[-2]*nums[-3]
        res2 = nums[0]*nums[1]*nums[-1]
        return max(res1,res2)

