"""
problem 86: Partition List
https://leetcode.com/problems/partition-list/

solution:

""" 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        smaller_head = ListNode(0)
        greater_head = ListNode(0)
        
        smaller = smaller_head
        greater = greater_head
        while head:
            if head.val < x:
                smaller.next = head
                smaller = head
            else:
                greater.next = head
                greater = head
            head = head.next
        greater.next = None
        smaller.next = greater_head.next
        return smaller_head.next





