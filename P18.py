"""
problem 18: 4 Sum
https://leetcode.com/problems/4sum/

solution:


""" 

class Solution:
    def fourSum(self, nums, target):
        result = set()
        nums.sort()
        length = len(nums)
        for idx_1, value_1 in enumerate(nums[:-3]):
            target_1 = target - value_1
            for idx_2, value_2 in enumerate(nums[idx_1 + 1:-2]):
                idx_2 += idx_1 + 1
                target_2 = target_1 - value_2
                high = length - 1
                low = idx_2 + 1
                while low < high:
                    total = nums[low] + nums[high]
                    if total < target_2:
                        low += 1
                    elif total > target_2:
                        high -= 1
                    else:
                        result.add((value_1, value_2, nums[low], nums[high]))
                        low += 1
                        high -= 1
        return [list(i) for i in result]

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        table = {}
        count = {}
        result = set()
        nums.sort()
        previous = None
        for idx_1, value_1 in enumerate(nums[:-1]):
            if value_1 == previous:
                count[previous] += 1
            else:
                previous = value_1
                count[value_1] = 1
            for value_2 in nums[idx_1 + 1:]:
                value = value_1 + value_2
                if value not in table:
                    table[value] = set()
                table[value].add((value_1, value_2))
        if nums[-1] == previous:
            count[previous] += 1
        else:
            count[nums[-1]] = 1

        look_up = sorted(table.items(), key=lambda x: x[0])

        for key in look_up:
            value = key[0]
            diff = target - value
            if diff < value:
                break
            elif diff == value:
                list1 = list(table[value])
                for idx, i in enumerate(list1):
                    for j in list1[idx:]:
                        for_append = i + j
                        for_append_table = {}
                        for k in for_append:
                            if k in for_append_table:
                                for_append_table[k] += 1
                            else:
                                for_append_table[k] = 1
                        for k, v in for_append_table.items():
                            if count[k] < v:
                                break
                        else:
                            result.add(tuple(sorted(for_append)))
            else:
                if diff in table:
                    list1 = table[value]
                    list2 = table[diff]
                    for i in list1:
                        for j in list2:
                            for_append = i + j
                            for_append_table = {}
                            for k in for_append:
                                if k in for_append_table:
                                    for_append_table[k] += 1
                                else:
                                    for_append_table[k] = 1
                            for k, v in for_append_table.items():
                                if count[k] < v:
                                    break
                            else:
                                result.add(tuple(sorted(for_append)))
        return [list(i) for i in result]

