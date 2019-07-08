class Solution:
    """
    @param array: the input array
    @return: the sorted array
    """

    def multiSort(self, array):
        # Write your code here
        array.sort(key=lambda x: x[0])
        array.sort(key=lambda x: x[1], reverse=True)
        return array


