"""
Problem 237. Delete Node in a Linked List
https://leetcode.com/problems/delete-node-in-a-linked-list/

solution:

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next:
            node.val = node.next.val
            if not node.next.next:
                node.next = None
            else:
                node = node.next
