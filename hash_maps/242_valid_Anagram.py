# Problem 2: Valid Anagram (Easy)

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Input: s = "rat", t = "car"
# Output: false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


s = "anagram"
t = "nagaram"
sol = Solution()
print(sol.isAnagram(s, t))


