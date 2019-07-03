class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """

    def validWordSquare(self, words):
        # Write your code here

        l = len(words)
        for i in range(l):
            row = []
            col = []

            row = list(words[i])
            lr = len(row)

            if lr > l:
                return False
            elif l > lr:
                return False

            for j in range(lr):
                col.append(words[j][i])

            if col != row:
                return False
            else:
                return True