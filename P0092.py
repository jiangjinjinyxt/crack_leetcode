"""
problem 92: Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/

solution:

""" 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        dummy_node = ListNode(0)
        dummy_node.next = head
        first = dummy_node
        count = 1
        while count < m:
            first = first.next
            count += 1
        previous = first.next
        current = previous.next
        count += 1
        while count < n:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            count += 1
        second = first.next
        first.next = current
        second.next = current.next
        current.next = previous
        return dummy_node.next






