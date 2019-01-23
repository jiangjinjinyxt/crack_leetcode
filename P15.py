"""
problem 15: 3Sum
https://leetcode.com/problems/3sum/

solution:
    Firstly, use a table(dict object) to store the apperance of 
        numbers in the list.
    Secondly, sort the table by numbers to get look_up(list obj).
    Thirdly, iterate through the table
        if the current number is bigger than 0, we know that the
        later numbers are all bigger than 0, so each three of their
        sum must be bigger than 0, we just break out the loop.
        if the current number if 0, numbers after 0 must be greater
        than 0, cannot form 0. Only if more than 2 0s in the table 
        can make an candidate.
        if the current number is smaller than 0, we form into the 
        next iteration(start from the current index or the next index)

"""  

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length <= 2:
            return []

        table = dict()
        
        result = []
    
        for i in nums:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        look_up = sorted(table.items(), key=lambda x: x[0])
        for idx, pair in enumerate(look_up):
            value = pair[0]
            nums = pair[1]
            # print(pair)
            if value > 0:
                continue
            if value == 0:
                if nums >= 3:
                    result.append([0] * 3)
                continue
            else:
                if nums == 1:
                    enum = look_up[idx + 1:]
                else:
                    enum = look_up[idx:]
            # print(enum)
            for _, pair_2 in enumerate(enum):
                value_2 = pair_2[0]
                nums_2 = pair_2[1]
                target = - (value + value_2)
                if target not in table:
                    continue
                if target < value_2:
                    break
                elif target == value_2:
                    if nums_2 >= 2:
                        result.append([value, value_2, value_2])
                else:
                    result.append([value, value_2, target])
        return result
        



