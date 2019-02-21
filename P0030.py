"""
problem 30: Substring with Concatenation of All Words
https://leetcode.com/problems/substring-with-concatenation-of-all-words/

solution:
    HASH TABLE

""" 

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        if not words:
            return result
        table = dict()
        for word in words:
            if word not in table:
                table[word] = 0
            table[word] += 1
        len_word = len(words[0])
        len_words = len(words)
        len_string = len(s)
        len_all_words = len_word * len_words
        for start_index in range(len_string + 1 - len_all_words):
            cur_table = dict()
            for index in range(start_index, start_index + len_all_words, len_word):
                cur_word = s[index:index+len_word]
                if cur_word in table:
                    if cur_word not in cur_table:
                        cur_table[cur_word] = 0
                    if cur_table[cur_word] >= table[cur_word]:
                        break
                    else:
                        cur_table[cur_word] += 1
                else:
                    break
            else:
                result.append(start_index)
        return result