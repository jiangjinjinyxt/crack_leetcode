"""
problem 139: Break Word
https://leetcode.com/problems/break-word/

solution:

""" 

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False] * len(s)
        for index in range(1, len(s) + 1):
            for word in wordDict:
                if len(word) == index:
                    if word == s[:index]:
                        dp[index - 1] = True
                        break
                elif len(word) < index:
                    if word == s[index - len(word):index] and dp[index - len(word) - 1]:
                        dp[index - 1] = True
                        break
        return dp[len(s) - 1]