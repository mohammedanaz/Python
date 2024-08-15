# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# 2 pointer technique

nums = [-1,0,1,2,-1,-4]

nums.sort()
result = []

for i in range(len(nums) - 2):
    left, right = i+1, len(nums)-1