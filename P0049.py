"""
problem 49: Group Anagrams
https://leetcode.com/problems/group-anagrams/

solution:

""" 
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        table = {
                    'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17,
                    'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 41, 'm': 43, 'n': 47,
                    'o': 53, 'p': 59, 'q': 61, 'r': 67, 's': 71, 't': 73, 
                    'u': 79, 'v': 83, 'w': 89, 'x': 97, 'y': 101, 'z':103
                }
        result = dict()
        for value in strs:
            total = 1
            for character in value:
                total *= table[character]
            if total not in result:
                result[total] = []
            result[total].append(value)
        return list(result.values())