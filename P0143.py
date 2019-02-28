"""
problem 143: ReOrder List
https://leetcode.com/problems/reorder-list/

solution:

""" 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            pass
        else:
            length = 0
            pseudo = head
            while pseudo:
                length += 1
                pseudo = pseudo.next
            first_tail = head
            for i in range(length // 2):
                first_tail = first_tail.next
            previous = first_tail.next
            first_tail.next = None
            current = previous.next
            previous.next = None
            while current:
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            second_head = previous
            first_head = head
            while second_head:
                first_next = first_head.next
                second_next = second_head.next
                first_head.next = second_head
                second_head.next = first_next
                first_head = first_next
                second_head = second_next