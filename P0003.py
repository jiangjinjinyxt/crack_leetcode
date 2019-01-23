"""
problem 3: Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

solution:
    1:  use a dictionary to record the largest index of
        the characters encoutered.
    2:  use a temp variable to record the smallest index, 
        between(exclusively) which and the current_index,
        there is no repeteness, range is (temp, current_index),
        so, till now, the maximum length of a substring is 
        at least:
            current_index - temp - 1
    3:  if current_char is in the dictionary,
            (1) if the index of the current_char recorded in dict 
                is in the range (temp, current_index), we need to 
                update the temp variable as dictionary[current_char],
                (no need to update maximum length)
            (2) if the index of the current_char recorded in dict
                is <= temp, no need to update the temp varible,
                but need to check whether current_index - temp is bigger
                than maximum length
            (3) update the dictionary(value of current_char)
        else
            only need to check whether it is needed to update maximum
            length

"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        previous_index = -1
        look_up = dict()
        max_len = 0
        for idx, value in enumerate(s):
            if value in look_up:
                if previous_index < look_up[value]:
                    previous_index = look_up[value]
                else:
                    temp_max = idx - previous_index
                    if temp_max > max_len:
                        max_len = temp_max
            else:
                temp_max = idx - previous_index
                if temp_max > max_len:
                    max_len = temp_max
            look_up[value] = idx
        return max_len
