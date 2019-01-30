"""
problem 44: Wildcard Matching
https://leetcode.com/problems/wildcard-matching/

solution:
    for every number which is in the range [0, length], try to
    put it in the right place(at index: number-1)
    works like this
        loop through the list
            at the current index, if the current value is not in 
            the range, continue
        step1   if the currnet value is in the range:
                if the current value is euql to the current index + 1,
                in the right place, continue
                else:
                    we need to try to put the value into the right 
                    place
                    we have to args now, current_value, current_index,
                    and current_value != current_index + 1
                    check the index = current_value - 1, this index is
                    the right place where current_value should be.
                    if the value at the index(current_value - 1) is not
                    equal to current_value(so, the value does not match
                    the index), we swap the two values, goto step1
            loop through the list again, return index + 1, if the value
            at the index is not equal to index + 1.
""" 
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        table = dict()
        table[(0, 0)] = True

        def find(i, j):
            if (i, j) not in table:
                if not i:
                    if p[j - 1] != '*':
                        ans = False
                    else:
                        ans = find(i, j - 1)
                elif not j:
                    ans = False
                else:
                    if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                        ans = find(i - 1, j - 1)
                    elif p[j - 1] == '*':
                        ans = find(i, j - 1) or find(i - 1, j)
                    else:
                        ans = False
                table[(i, j)] = ans
            return table[(i, j)]

        return find(len(s), len(p))