"""
problem 14: Longest Commom Prefix
https://leetcode.com/problems/longest-common-prefix/

solution:
    just iterate.

"""  

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_common = ""
        if not strs:
            return longest_common
        max_len = min([len(_) for _ in strs])
        
        index = 0
        while index < max_len:
            prefix = strs[0][index]
            for i in strs[1:]:
                if i[index] != prefix:
                    return longest_common
            longest_common += prefix
            index += 1
        return longest_common



