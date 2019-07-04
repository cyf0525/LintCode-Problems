class Solution:
    """
    @param letters: a list of sorted characters
    @param target: a target letter
    @return: the smallest element in the list that is larger than the given target
    """

    def nextGreatestLetter(self, letters, target):
        # Write your code here
        for ch in letters:
            if ch > target:
                return ch

