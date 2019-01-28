"""
problem 32: Longest Valid Parentheses
https://leetcode.com/problems/longest-valid-parentheses/

solution:
    https://leetcode.com/problems/longest-valid-parentheses/solution/
    DP:
    Use a table(length equal to s) to store the length of the longest 
    valid substring ending at iith index.
    The table is initialized with 0's.
    At index i, if s[i] is ')' and s[i - 1] is '(', then table[i] = table[i - 2] + 2
                if s[i] is ')' and s[i - 1] is ')', then the next index we need to
                check is: i - table[i - 1] - 1, if s[i - table[i - 1] - 1] is '(',
                table[i] = table[i - 1] + table[i - table[i - 1] - 2] + 2
""" 
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        left_paren = '('
        right_paren = ')'
        length = len(s)
        table = [0] * length
        for index in range(1, length):
            if s[index] == right_paren:
                if s[index - 1] == left_paren:
                    if index >= 2:
                        table[index] = table[index - 2] + 2
                    else:
                        table[index] = 2
                else:
                    temp_index = index - table[index - 1] - 1
                    if temp_index >= 0 and s[temp_index] == '(':
                        if temp_index > 0:
                            table[index] = table[temp_index - 1] + table[index - 1] + 2
                        else:
                            table[index] = table[index - 1] + 2
        return max(table)