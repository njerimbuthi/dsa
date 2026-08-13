# Problem:      Remove Element (LC 27)
# Goal:         Remove all occurrences of val in-place, return count of remaining
# Brute:        New list + copy back → O(n) time, O(n) space
# Optimal:      Read/write two-pointer → O(n) time, O(1) space
# Invariant:    Everything left of write contains only kept elements
# Tradeoff:     —
# Pattern:      P6: In-place Array Manipulation (read/write pointer)
# Signal:       "In-place," "remove," "return count of remaining"
# Key trick:    Write pointer only advances on kept elements
# Edge cases:   Empty array, all elements equal val, no elements equal val


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        write = 0

        for i, num in enumerate(nums):
            if num == val:
                continue
            nums[write] = num
            write += 1
        return write


nums = [3, 2, 2, 3]
val = 3
sol = Solution()
k = sol.removeElement(nums, val)
print(k)
print(nums[:k])
