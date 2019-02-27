"""
problem 109. Convert Sorted List to Binary Search Tree
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

solution:

""" 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        table = []
        while head:
        	table.append(head.val)
        	head = head.next

        def helper(left, right):
        	if left > right:
        		return None
        	elif left == right:
        		return TreeNode(table[left])
        	else:
        		middle = left + (right - left) // 2
        		node = TreeNode(table[middle])
        		node.left = helper(left, middle - 1)
        		node.right = helper(middle + 1, right)
        		return node
        return helper(0, len(table) - 1)

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
       	size = 0
       	dummy = head
       	while dummy:
       		size += 1
       		dummy = dummy.next
       	dummy = head
       	def convert(left, right):
       		global dummy
       		if left > right:
       			return None
       		middle = left + (right - left) // 2
       		left = convert(left, middle -  1)
       		node = TreeNode(dummy.val)
       		node.left = left
       		dummy = dummy.next
       		node.right = convert(middle + 1, right)
       		return node
       	return convert(0, size - 1)