# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# 2 pointer technique

nums = [-1,0,1,2,-1,-4]

nums.sort()
result = []

for i in range(len(nums) - 2):
    if i>0 and nums[i] == nums[i-1]:
        continue

    left, right = i+1, len(nums)-1

    while left < right:
        sum = nums[i] + nums[left] + nums[right]

        if sum == 0:
            result.append([nums[i],nums[left],nums[right]])

            #avoid duplicate values of left, right
            while left < right and nums[left+1] == nums[left]:
                left += 1
            while left < right and nums[right-1] == nums[right]:
                right -= 1
            left += 1
            right -= 1

        elif sum < 0:
            left += 1
        else:
            right -= 1

print(result)