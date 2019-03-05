"""
Problem 234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

solution:

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result == result[::-1]