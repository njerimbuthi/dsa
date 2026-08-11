# Problem:      Merge Sorted Array (LC 88)
# Goal:         Merge two sorted arrays in-place into nums1
# Brute:        Copy + sort → O((m+n) log(m+n))
# Optimal:      Three pointers from the back → O(m+n), O(1) space
# Invariant:    Everything to the right of write is correctly placed
# Tradeoff:     Using the pre-allocated space vs needing extra memory
# Pattern:      In-place Array Manipulation / Backward Merge
# Signal:       "Sorted," "in-place," "extra space at the end"
# Key trick:    Fill from back so writes never destroy unread data
# Edge cases:   nums2 empty (nothing to do), nums1 empty (copy all of nums2)

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1
        write = (m + n) - 1

        while (p1 >= 0) and (p2 >= 0):
            if nums1[p1] >= nums2[p2]:
                nums1[write] = nums1[p1]
                p1 -= 1  # move the source pointer
            else:
                nums1[write] = nums2[p2]
                p2 -= 1  # move the other source pointer
            write -= 1  # always moves

        while p2 >= 0:
            nums1[write] = nums2[p2]
            p2 -= 1
            write -= 1


# Test cases
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
n = 3

sol = Solution()
print(sol.merge(nums1, m, nums2, n))
