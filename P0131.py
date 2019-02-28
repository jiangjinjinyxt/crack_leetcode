"""
problem 131. Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/

solution:

""" 
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        if not s:
            return result
        
        def is_palindrome(string):
            if string == string[::-1]:
                return True
            else:
                return False
        
        def dfs(ans, string):
            if not string:
                result.append(ans)
            else:
                for index in range(1, len(string) + 1):
                    if is_palindrome(string[:index]):
                        dfs(ans + [string[:index]], string[index:])
        dfs([], s)
        return result