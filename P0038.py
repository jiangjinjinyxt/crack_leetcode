"""
problem 38: Count And Say
https://leetcode.com/problems/count-and-say/

solution:

""" 
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        count = self.countAndSay(n - 1)
        say = ''

        previous = count[0]
        number = 1
        for value in count[1:]:
            if value == previous:
                number += 1
            else:
                say += str(number) + previous
                previous = value
                number = 1
        say += str(number) + previous
        return say