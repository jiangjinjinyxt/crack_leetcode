class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        look_up = dict()
        for i in nums:
        	if i in look_up:
        		look_up[i] += 1
        	else: 
        		look_up[i] = 1
        look_up = sorted(look_up.items(), key=lambda x: x[0])
        dp = [0] * (len(look_up) + 1)
        dp[1] = look_up[0][0] * look_up[0][1]
        previous = look_up[0][0]
        for idx, value in enumerate(look_up[1:]):
        	idx += 1
        	temp = value[0] * value[1]
        	if previous == value[0] - 1:
        		dp[idx + 1] = max(dp[idx], dp[idx - 1] + temp)
        	else:
        		dp[idx + 1] = dp[idx] + temp
        	previous = value[0]
        return dp[-1]

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = max(nums)
        dp = [0] * (maximum + 1)

        for value in nums:
        	dp[value] += value

        idx_2, idx_1 = 0, 0
        for value in dp[1:]:
        	temp = max(idx_1, idx_2 + value)
        	idx_2, idx_1 = idx_1, temp
        return idx_1
