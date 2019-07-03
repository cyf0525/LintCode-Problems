class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        nums.sort()
        mid = (len(nums))/2
        res = nums[mid]
        return res
