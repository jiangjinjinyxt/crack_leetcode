"""
problem 147: Insertion Sort List
https://leetcode.com/problems/insertion-sort-list/

solution:

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        loop_head = head.next
        head.next = None
        dummy_head = ListNode(float('inf'))
        dummy_head.next = head
        while loop_head:
            next_head = loop_head.next
            temp = dummy_head
            while temp.next and temp.next.val > loop_head.val:
                temp = temp.next
            tail = temp.next
            temp.next = loop_head
            loop_head.next = tail
            loop_head = next_head
        def reverse_list(node):
            previous = node
            current = node.next
            previous.next = None
            while current:
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            return previous
        return reverse_list(dummy_head.next)

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = dummy = ListNode(0)
        cur = dummy.next = head
        while cur and cur.next:
            val = cur.next.val
            if cur.val < val:
                cur = cur.next
                continue
            if p.next.val > val:
                p = dummy
            while p.next.val < val:
                p = p.next
            new = cur.next
            cur.next = new.next
            new.next = p.next
            p.next = new
        return dummy.next
    


