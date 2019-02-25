"""
problem 61: Rotate List
https://leetcode.com/problems/rotate-list/

solution:
https://leetcode.com/problems/rotate-list/solution/
""" 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k or not head.next:
            return head

        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        current.next = head
        for i in range(length - k % length - 1):
            head = head.next
        new_head = head.next
        head.next = None
        return new_head


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not k:
            return head
        dummy = ListNode(0)
        dummy.next = head

        length = 0
        previous = dummy
        while previous.next and length < k:
            length += 1
            previous = previous.next
        if not previous.next:
            k %= length
            previous = dummy
            for i in range(k):
                previous = previous.next
        current = dummy
        while previous.next:
            current = current.next
            previous = previous.next
        if not current.next:
            return head
        ans = current.next
        previous.next = head
        current.next = None
        return ans