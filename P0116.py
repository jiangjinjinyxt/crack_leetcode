"""
problem 116. Populating Next Right Pointers in Each Node
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

solution:

""" 
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        head = root
        while head:
        	temp = head
        	while temp:
        		if temp.left:
        			temp.left.next = temp.right
        			if temp.next:
        				temp.right.next = temp.next.left
        			else:
        				temp.right.next = None
        		temp = temp.next
        	head = head.left
        return root


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        stack = []
        if root:
        	stack.append(root)

        while stack:
        	size = len(stack)
        	previous_node = stack.pop(0)
        	if previous_node.left:
        		stack.append(previous_node.left)
        	if previous_node.right:
        		stack.append(previous_node.right)
        	size -= 1
        	while size:
        		size -= 1
        		current_node = stack.pop(0)
        		previous_node.next = current_node
        		previous_node = current_node
	        	if previous_node.left:
	        		stack.append(previous_node.left)
	        	if previous_node.right:
	        		stack.append(previous_node.right)
	        previous_node.next = None
        return root