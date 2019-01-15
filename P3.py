"""
problem 3: Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

solution:
	dynamic programming
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
        return max_len
