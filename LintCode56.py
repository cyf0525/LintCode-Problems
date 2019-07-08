class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
		# write your code here
		maps = {}
		for i in range(len(numbers)):
				if numbers[i] in maps:
						return [maps.get(numbers[i]), i]
				else:
				    maps[target - numbers[i]] = i

