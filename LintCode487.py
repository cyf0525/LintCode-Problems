class Solution:
    """
    @param names: a string array
    @return: a string array
    """

    def nameDeduplication(self, names):
        # write your code here
        d = {}
        result = []

        for name in names:
            name = name.lower()
            if name not in d:
                d[name] = 1
                result.append(name)
        return result

