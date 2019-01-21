"""
problem 19: Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

solution:
    https://leetcode.com/problems/remove-nth-node-from-end-of-list/solution/

"""  
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy_head = ListNode(0)
        dummy_head.next = head
        head_1 = dummy_head
        head_2 = dummy_head
        for i in range(n):
            head_2 = head_2.next
        while head_2.next is not None:
            head_1 = head_1.next
            head_2 = head_2.next
        head_1.next = head_1.next.next
        return dummy_head.next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy_head = ListNode(0)
        dummy_head.next = head
        length = 0
        while head:
            length += 1
            head = head.next
        head = dummy_head
        for i in range(length - n):
            head = head.next
        head.next = head.next.next
        return dummy_head.next

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not n:
            return head
        
        temp = head
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next
        if n == length:
            return head.next
        temp = head
        for i in range(length - n - 1):
            temp = temp.next
        temp.next = temp.next.next

        return head

