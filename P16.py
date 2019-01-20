"""
problem 16: 3Sum Cloest
https://leetcode.com/problems/3sum-closest/

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
    def threeSumClosest(self, nums, target):
        nums.sort()
        total = nums[0] + nums[1] + nums[2]
        diff = abs(total - target)
        if not diff:
            return target
        length = len(nums)
        for idx, value in enumerate(nums[:-2]):
            low = idx + 1
            high = length - 1
            while low < high:
                temp_total = value + nums[low] + nums[high]
                if temp_total == target:
                    return temp_total
                else:
                    if abs(temp_total - target) < diff:
                        total = temp_total
                        diff = abs(temp_total - target)
                    if temp_total > target:
                        high -= 1
                    else:
                        low += 1
        return total
                
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        look_up = dict()
        for i in nums:
            if i in look_up:
                look_up[i] += 1
            else:
                look_up[i] = 1

        table = sorted(look_up.items(), key=lambda x: x[0])
        cloest = float('inf')
        length = len(table)
        def binary_search_cloest(begin, end, target_value):
            if begin > end:
                return float('inf')
            if table[begin][0] >= target_value:
                return table[begin][0]
            if table[end][0] <= target_value:
                return table[end][0]
            candidate = table[begin][0]
            if abs(table[end][0] - target_value) < abs(candidate - target_value):
                candidate = table[end][0]
            middle = begin + (end - begin) // 2
            if table[middle][0] == target_value:
                return target_value
            elif table[middle][0] > target_value:
                if abs(table[middle][0] - target_value) < abs(candidate - target_value):
                    candidate = table[middle][0]
                find_value = binary_search_cloest(begin, middle - 1, target_value)
                if abs(find_value - target_value) < abs(candidate - target_value):
                    return find_value
                else:
                    return candidate
            else:
                if abs(table[middle][0] - target_value) < abs(candidate - target_value):
                    candidate = table[middle][0]
                find_value = binary_search_cloest(middle + 1, end, target_value)
                if abs(find_value - target_value) < abs(candidate - target_value):
                    return find_value
                else:
                    return candidate


        cloest = float('inf')
        cloest_pair = [0, 0, 0]
        length = len(table)
        for idx_1, pair_1 in enumerate(table):
            value_1 = pair_1[0]
            nums_1 = pair_1[1]
            if nums_1 > 1:
                for idx_2, pair_2 in enumerate(table[idx_1:]):
                    idx_2 += idx_1
                    value_2 = pair_2[0]
                    nums_2 = pair_2[1]
                    target_value = target - value_1 - value_2
                    if (idx_2 == idx_1 and nums_2 == 2) or (nums_2 == 1):
                        # target_value = target - value_1 - value_2
                        if value_2 >= target_value:
                            if idx_2 < length - 1:
                                value_3 = table[idx_2 + 1][0]
                                if abs(value_1 + value_2 + value_3 - target) < cloest:
                        # print('jaj')
                                    cloest = abs(value_1 + value_2 + value_3 - target)
                                    cloest_pair = [value_1, value_2, value_3]
                            break
                        value_3 = binary_search_cloest(idx_2 + 1, length - 1, target_value)
                    else:
                        if value_2 >= target_value:
                            value_3 = value_2
                            if abs(value_1 + value_2 + value_3 - target) < cloest:
                        # print('jaj')
                                cloest = abs(value_1 + value_2 + value_3 - target)
                                cloest_pair = [value_1, value_2, value_3]
                            break
                        value_3 = binary_search_cloest(idx_2, length - 1, target_value)
                    if abs(value_1 + value_2 + value_3 - target) < cloest:
                        # print('jaj')
                        cloest = abs(value_1 + value_2 + value_3 - target)
                        cloest_pair = [value_1, value_2, value_3]
            else:
                for idx_2, pair_2 in enumerate(table[idx_1 + 1:]):
                    idx_2 += idx_1 + 1
                    value_2 = pair_2[0]
                    nums_2 = pair_2[1]
                    target_value = target - value_1 - value_2
                    if nums_2 == 1:
                        if value_2 >= target_value:
                            if idx_2 < length - 1:
                                value_3 = table[idx_2 + 1][0]
                                if abs(value_1 + value_2 + value_3 - target) < cloest:
                        # print('jaj')
                                    cloest = abs(value_1 + value_2 + value_3 - target)
                                    cloest_pair = [value_1, value_2, value_3]
                            break
                        value_3 = binary_search_cloest(idx_2 + 1, length - 1, target_value)
                    else:
                        if value_2 >= target_value:
                            value_3 = value_2
                            if abs(value_1 + value_2 + value_3 - target) < cloest:
                        # print('jaj')
                                cloest = abs(value_1 + value_2 + value_3 - target)
                                cloest_pair = [value_1, value_2, value_3]
                            break                            
                        value_3 = binary_search_cloest(idx_2, length - 1, target_value)
                    if abs(value_1 + value_2 + value_3 - target) < cloest:
                        # print('here')
                        cloest = abs(value_1 + value_2 + value_3 - target)
                        cloest_pair = [value_1, value_2, value_3]
        # print(cloest_pair)
        return sum(cloest_pair)
                    



