"""
problem 647: palindromic substring
https://leetcode.com/problems/palindromic-substrings/description//description/

solution:
	dynamic programming
"""
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # initialize array
        length = len(s)
        result = [[False] * length for i in range(length)]
        equal_sequence = list(range(length))
        for idx in range(1, length):
        	if s[idx] == s[idx - 1]:
        		equal_sequence[idx] = equal_sequence[idx - 1]
        for i in range(length):
        	result[i][i] = True

        total = length
        for window_size in range(2, length + 1):
        	for row in range(length - window_size + 1):
        		column = row + window_size - 1
        		if (equal_sequence[column] <= row) or (result[row + 1][column - 1] and s[row] == s[column]):
        			result[row][column] = True
        			total += 1

        """
        for row in range(length - 1):
        	for column in range(row + 1, length):
        		print(row, column)
        		if (equal_sequence[column] <= row) or (result[row + 1][column - 1] and s[row] == s[column]):
        			result[row][column] = True
        			print("True for {} {}".format(row, column))
        			total += 1
        """
        return total


