"""
Problem 205: Isomorphic Strings

https://leetcode.com/problems/isomorphic-strings/
solution:

"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        table = dict()
        mapped = set()
        if len(s) != len(t):
        	return False

        for idx, value in enumerate(s):
        	if value in table:
        		if table[value] == t[idx]:
        			continue
        		else:
        			return False
        	else:
        		if t[idx] in mapped:
        			return False
        		else:
        			table[value] = t[idx]
        			mapped.add(t[idx])
        return True