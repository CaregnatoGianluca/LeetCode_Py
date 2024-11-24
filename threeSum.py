from typing import List

"""Given an integer array nums, 
return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets."""

class threesum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if (nums[i] + nums[j] + nums[k]) == 0 and sorted([nums[i], nums[j], nums[k]]) not in ret:
                        ret.append(sorted([nums[i], nums[j], nums[k]]))

        return ret
