# https://leetcode.com/problems/two-sum/
from itertools import combinations

class Solution(object):
    def twoSum(self, nums, target):
        answer=[]
        target_cans=combinations(nums,2)
        for i in target_cans:
            if sum(i)==target :
                answer.append(nums.index(i[0]))
                nums[nums.index(i[0])]='X'
                answer.append(nums.index(i[1]))
        return answer