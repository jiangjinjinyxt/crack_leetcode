"""
Problem 206: Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/
solution:

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        pre = head
        cur = head.next
        pre.next = None
        while cur.next:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        cur.next = pre
        return cur