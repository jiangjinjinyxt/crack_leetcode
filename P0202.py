"""
problem 202: Happy Number
https://leetcode.com/problems/happy-number/

solution:

"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        def helper(number):
            if number == 1:
                return True
            if number in visited:
                return False
            visited.add(number)
            count = 0
            while number:
                count += (number % 10) ** 2
                number //= 10
            return helper(count)
        return helper(n)

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def helper(number):
            count = 0
            while number:
                count += (number % 10) ** 2
                number //= 10
            return count
        slow = n
        fast = helper(n)
        while fast != 1 and slow != fast:
            slow = helper(slow)
            fast = helper(helper(fast))
        if fast == 1:
            return True
        else:
            return False


