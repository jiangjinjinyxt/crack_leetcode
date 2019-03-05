"""
Problem 1002. Find Common Characters
https://leetcode.com/problems/find-common-characters/

solution:

"""
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        table = dict()
        ans = []
        if not A:
            return ans
        for i in A[0]:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        
        for string in A[1:]:
            if not table:
                return []
            temp_dict = dict()
            for char in string:
                if char in table:
                    if char in temp_dict:
                        temp_dict[char] += 1
                    else:
                        temp_dict[char] = 1
            keys_to_delete = []
            for key, value in table.items():
                if key not in temp_dict:
                    keys_to_delete.append(key)
                else:
                    if value > temp_dict[key]:
                        table[key] = temp_dict[key]
            for key in keys_to_delete:
                del table[key]
        result = []
        for key, value in table.items():
            result.extend([key] * value)
        return result