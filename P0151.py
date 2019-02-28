"""
Problem 151. Reverse Words in a String
https://leetcode.com/problems/reverse-words-in-a-string/
solution:

"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        temp = ""
        for char in s:
            if char == " ":
                if temp:
                    if ans:
                        ans = temp + " " + ans
                    else:
                        ans = temp
                    temp = ""
            else:
                temp += char
        if temp:
            if ans:
                ans = temp + " " + ans
            else:
                ans = temp
        return ans