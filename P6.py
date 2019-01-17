"""
problem 6: ZigZag Conversion
https://leetcode.com/problems/zigzag-conversion/

solution:
	string
"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = ""
        length = len(s)
        for row in range(numRows):
            index = row
            if (row == 0) or (row == numRows - 1):
                while index < length:
                    result += s[index]
                    index += 2 * numRows - 2
            else:
                while index < length:
                    result += s[index]
                    middle_index = index + 2 * (numRows - row - 1)
                    if middle_index < length:
                        result += s[middle_index]
                    index += 2 * numRows - 2
        return result


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        length = len(s)
        result = [""] * length
        ind = 0
        for row in range(numRows):
            index = row
            if (row == 0) or (row == numRows - 1):
                while index < length:
                    result[ind] = s[index]
                    ind += 1
                    index += 2 * numRows - 2
            else:
                while index < length:
                    result[ind] = s[index]
                    ind += 1
                    middle_index = index + 2 * (numRows - row - 1)
                    if middle_index < length:
                        result[ind] = s[middle_index]
                        ind += 1
                    index += 2 * numRows - 2
        return "".join(result)


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        if numRows <= 1 or numRows >= length:
            return s

        result = [""] * numRows
        numRows -= 1
        index = 0
        for character in s:
            result[index] += character
            if index == numRows:
                step = -1
            if index == 0:
                step = 1
            index += step
        return "".join(result)