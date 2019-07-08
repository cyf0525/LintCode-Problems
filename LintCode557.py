class Solution:
    """
    @param: : a string
    @return: Return a hash map
    """

    def countCharacters(self, str):
        # write your code here
        res = {}
        for letter in str:
            res[letter] = str.count(letter)

        return res