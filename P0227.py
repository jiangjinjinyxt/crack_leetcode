"""
Problem 227. Basic Calculator II
https://leetcode.com/problems/basic-calculator-ii/

solution:

"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """     
        stack = []
        current = ""
        operator = "+"
        for char in s:
            if char == " ":
                continue
            elif char.isdigit():
                current += char
            else:
                if operator == "*":
                    stack.append(stack.pop() * int(current))
                elif operator == "/":
                    stack.append(int(stack.pop() / int(current)))
                elif operator == "+":
                    stack.append(int(current))
                else:
                    stack.append(-int(current))
                operator = char
                current = ""
        # TO SKIP THIS PART, let s += '+' initially
        if current:
            if operator == "*":
                stack.append(stack.pop() * int(current))
            elif operator == "/":
                stack.append(int(stack.pop() / int(current)))
            elif operator == "+":
                stack.append(int(current))
            else:
                stack.append(-int(current))        
        return sum(stack)



