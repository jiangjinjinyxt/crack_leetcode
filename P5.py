"""
problem 5: Longest Palindromic Substring
https://leetcode.com/problems/median-of-two-sorted-arrays/

solution:
    Dynamic programming

Detailed explanation:
    https://leetcode.com/problems/longest-palindromic-substring/solution/
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        length = len(s)
        # print(length)
        longest = s[0]
        look_up = [[None] * length for i in range(length)]
        for i in range(length - 1):
            look_up[i][i] = 1
            if s[i] == s[i + 1]:
                look_up[i][i + 1] = 1
                longest = s[i:i+2]
        look_up[length - 1][length - 1] = 1
        
        for length_ in range(3, length + 1):
            for start in range(length - length_ + 1):
                end = start + length_ - 1
                # print(start, end, start + 1, end - 1)
                if s[start] == s[end] and look_up[start + 1][end - 1]:
                    look_up[start][end] = 1
                    longest = s[start:end+1]
        return longest