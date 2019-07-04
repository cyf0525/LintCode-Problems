class Solution:
    """
    @param words: a list of strings
    @return: return a list of strings
    """

    def findWords(self, words):
        # write your code here
        keyboard = [
            set('QWERTYUIOP'),
            set('ASDFGHJKL'),
            set('ZXCVBNM'),

        ]

        result = []
        for word in words:
            for row in keyboard:
                if set(word.upper()) <= row:
                    result.append(word)
        return result