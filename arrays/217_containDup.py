# Given an integer array nums,
# return true if any value appears at least twice in the array
# return false if every element is distinct.


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))


sol = Solution()
nums = [1, 2, 3, 4]
print(sol.containsDuplicate(nums))
