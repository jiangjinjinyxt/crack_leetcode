"""
problem 187. Repeated DNA Sequences
https://leetcode.com/problems/repeated-dna-sequences/

solution:

"""
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        if len(s) < 11:
        	return ans
        table = dict()
        start = s[:10]
        table[start] = 1
        for char in s[10:]:
        	start = start[1:] + char
        	if start in table:
        		if table[start] < 2:
        			table[start] += 1
        			ans.append(start)
        	else:
        		table[start] = 1
        return ans