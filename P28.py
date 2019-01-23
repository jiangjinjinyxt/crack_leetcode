"""
problem 28: Implement strStr()
https://leetcode.com/problems/implement-strstr/

solution:
    rabin-karp
    kmp

""" 
# kmp
class Solution:
    def strStr(self, sequence, sub_sequence):
        len_sub = len(sub_sequence)
        len_seq = len(sequence)
        if len_seq < len_sub:
            return -1
        if not len_sub:
            return 0
        sub_auxiliary = self.preprocessing(sub_sequence, len_sub)
        index_sub = 0
        index_seq = 0
        while index_seq < len_seq:
            if sequence[index_seq] == sub_sequence[index_sub]:
                index_seq += 1
                index_sub += 1
                if index_sub == len_sub:
                    return index_seq - len_sub
            else:
                if index_sub:
                    index_sub = sub_auxiliary[index_sub - 1]
                else:
                    index_seq += 1
        return -1


    @staticmethod
    def preprocessing(sub_sequence, len_sub):
        auxiliary = [0] * len_sub
        i, j = 1, 0
        while i < len_sub:
            if sub_sequence[i] == sub_sequence[j]:
                j += 1
                auxiliary[i] = j
                i += 1
            else:
                if j:
                    j = auxiliary[j - 1]
                else:
                    i += 1
        return auxiliary


# rabin-karp, use rolling hash
class Solution:
    def strStr(self, sequence, sub_sequence):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_sub = len(sub_sequence)
        len_seq = len(sequence)
        if len_sub > len_seq:
            return -1
        self.set_param(26, 113)
        self.magic = self.modulous - (self.base ** len_sub) % self.modulous
        current_index = len(sub_sequence)
        target = self.sequence_hash(sub_sequence)
        self.hash = self.sequence_hash(sequence[:current_index])
        while True:
            # print(sequence[current_index-len_sub:current_index])
            # print(self.hash)
            if target == self.hash:
                for idx in range(len_sub):
                    if sub_sequence[idx] != sequence[current_index - len_sub + idx]:
                        break
                else:
                    return current_index - len_sub
            if current_index == len_seq:
                return -1
            self.rolling(ord(sequence[current_index - len_sub]) - 97, ord(sequence[current_index]) - 97)
            current_index += 1

    def sequence_hash(self, sequence):
        total = 0
        for idx, value in enumerate(sequence[::-1]):
            total += ((ord(value) - 97) * self.base ** idx) % self.modulous
        return total % self.modulous
    
    def set_param(self, base, modulous):
        self.base = base
        self.modulous = modulous
        
    def rolling(self, old, new):
        self.hash = (self.hash * self.base + self.magic * old + new)
        print(self.hash)
        self.hash %= self.modulous