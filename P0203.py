"""
Problem 203. Remove Linked List Elements

https://leetcode.com/problems/remove-linked-list-elements/
solution:

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next