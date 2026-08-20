class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count_dict = {}

        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        return max(count_dict, key=lambda x: count_dict[x])

sol = Solution()
nums = [3,2,3]
print(sol.majorityElement(nums)) 


