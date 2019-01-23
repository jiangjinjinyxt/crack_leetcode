"""
problem 2: add two numbers
https://leetcode.com/problems/add-two-numbers/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        copy_head = head
        previous_mod = 0
        while l1 and l2:
        	previous_mod += l1.val + l2.val
        	copy_head.next = ListNode(previous_mod % 10)
        	previous_mod //= 10
        	l1 = l1.next
        	l2 = l2.next
        	copy_head = copy_head.next
        while l1:
        	previous_mod += l1.val
        	copy_head.next = ListNode(previous_mod % 10)
        	previous_mod //= 10
        	l1 = l1.next
        	copy_head = copy_head.next
        while l2:
        	previous_mod += l2.val
        	copy_head.next = ListNode(previous_mod % 10)
        	previous_mod //= 10
        	l2 = l2.next
        	copy_head = copy_head.next
        if previous_mod:
        	copy_head.next = ListNode(previous_mod)

        return head.next

