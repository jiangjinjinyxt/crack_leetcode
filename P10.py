"""
problem 10: Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/

solution:
    Condition 1:
        s is empty
            p is empty
                match
            p is not empty
                but the length of p is even, and the 
                character at odd indices is always '*', 
                the character at even indices is always 
                not '*', then 
                    match
                else
                    do not match
        s is not empty
            p is empty
                do not match
            p is not empty
                if p[0] == '.' or p[0] == s[0], this means the
                fisrt char matches, we need to look at the 
                second indice of p
                    if length of p is 1
                        check whether s[1:] is empty
                    else
                        if p[1] != '*'
                            p[:2] is '.*' or 'a*'
                            p[:2] can match s[0] >= 0 times
                            so check
                                if match zero times
                                    check p and s[2:]
                                if match >= 1 times
                                    recursively check p[1:] and s
                        else
                            (recursive) check whether p[1:] matches s[1:]
                else p[0] and s[0] does not match
                    only when len of p > 1 and p[1] == '*' can still make
                    macth happen
                        then check s and p[2:]

"""  

class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

class Solution:
    char_matcher = '.'
    num_matcher = '*'
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        len_s = len(s)
        len_p = len(p)

        if not len_s:
            if not len_p:
                return True
            elif len_p % 2 == 1:
                return False
            else:
                if p[0] == self.num_matcher:
                    return False
                elif p[1] == self.num_matcher:
                    return self.isMatch(s, p[2:])
                else:
                    return False

        if not len_p:
            return False

        if p[0] == self.char_matcher or p[0] == s[0]:
            if len_p > 1 and p[1] == self.num_matcher:
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            else:
                return self.isMatch(s[1:], p[1:])
        else:
            if len_p > 1 and p[1] == self.num_matcher:
                return self.isMatch(s, p[2:])
            else:
                return False