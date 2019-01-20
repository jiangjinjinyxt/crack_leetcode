"""
problem 12: Roman to Integer
https://leetcode.com/problems/roman-to-integer/

solution:
    Use a dictionary to store integer value in roman,
    for extension.

    Start from end to begin, once the integer value of
    the current roman char is greater than the previous
    one, we only need add the current integer value to 
    the total value,
    else, we need to minus the curret interger value from
    the total value.

"""  

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
                }

        length = len(s)
        current_index = length - 1
        result = 0
        previous_value = -1
        while current_index > -1:
            current_value = table[s[current_index]]
            if current_value >= previous_value:
                result += current_value
            else:
                result -= current_value
            previous_value = current_value
            current_index -= 1
        return result

