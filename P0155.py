"""
problem 155: Min Stack
https://leetcode.com/problems/min-stack/

solution:

""" 
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x < self.minimum:
            self.minimum = x
        self.stack.append((x, self.minimum))

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
            if self.stack:
                self.minimum = self.stack[-1][1]
            else:
                self.minimum = float('inf')

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
    
    def getMin(self):
        """
        :rtype: int
        """
        if stack:
            return self.minimum
        else:
            return None
    