"""
problem 17: Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

solution:


"""  
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        table = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []

        for digit in digits:
            if not result:
                result = [_ for _ in table[digit]]
            else:
                result = [i + _ for i in result for _ in table[digit]]
        return result

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dictionary = {'2': "abc", '3':"def", '4':"ghi", '5':'jkl', '6':"mno",'7':'pqrs',
                     '8':"tuv", "9":"wxyz"}
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return list(dictionary[digits])
        else:
            first = dictionary[digits[0]]
            second = self.letterCombinations(digits[1:])
            return [i + j for i in first for j in second]