"""
problem 20: Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

solution:
    https://leetcode.com/problems/valid-parentheses/solution/

"""  

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paren_dict = {
            '(': ')',
            '[': ']',
            '{': '}'
            }
        
        previous_parentheses = []
        for paren in s:
            if paren in paren_dict:
                previous_parentheses.append(paren)
            else:
                if not previous_parentheses:
                    return False
                left = previous_parentheses.pop()
                if paren != paren_dict[left]:
                    return False
        if not previous_parentheses:
            return True
        else:
            return False
