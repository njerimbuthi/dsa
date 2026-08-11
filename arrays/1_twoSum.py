# ──────────────────────────────────────────────────
# Problem: Two Sum
# ──────────────────────────────────────────────────
# Goal:       Find two indices whose values add up to target.
# Brute:      Nested loop checking every pair — O(n²) time, O(1) space.
# Optimal:    Hash map complement lookup — O(n) time, O(n) space.
# Invariant:  At every iteration, `seen` contains every number
#             visited so far mapped to its index. If the complement
#             exists in `seen`, the pair was guaranteed to be found.
# Tradeoff:   Spent O(n) memory (dictionary) to eliminate O(n) inner search.
#             Traded space for time.
# Pattern:    Complement Lookup (single-pass hash map)
# Signal:     "Find a pair that satisfies an equation" →
#             rewrite as "for each element, does its partner exist?"
# Key trick:  a + b = target  →  b = target - a  →  look up b in dict.
# Edge case:  Duplicate values [3, 3] work because you check before storing.
# ──────────────────────────────────────────────────


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Find indices of two numbers that sum to target.

        Geometric intuition: walk through the number line once.
        At each position, check if the 'mirror' number
        (target - current) has been seen before.

        Time:  O(n) — single pass through nums
        Space: O(n) — seen dict grows linearly with n

        Invariant: seen contains only indices < i at time of lookup,
                preventing self-pairing on duplicate values.
        """
        seen: dict[int, int] = {}  # value → index

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        raise ValueError(f"No valid pair sums to {target}")


nums = [2, 7, 11, 15]
target = 9

sol = Solution()
print(sol.twoSum(nums, target))


# ____________NOTES______________

# PATTERN 1: Brute Force First — Then Ask "What's Slow?"
# Before the clever solution, there's always the obvious one.
# For Two Sum, the brute force is: check every pair.
# Two nested loops.
# For every number, you scan through every other number after it.
# It works. But it's slow.
# Why is this useful to write first?
# Because it shows you exactly where the waste is.
# The inner loop is doing one thing: searching for a number that completes the pair.
# That search is the bottleneck. The entire optimization is about making that search faster.
# Mental model: always start by asking "what is my code searching for repeatedly, and can I make that search instant?"


# PATTERN 2: Trade Space for Time
# This is the single most common optimization pattern in all of computer science.
# The idea is simple — if something is slow to find, store it somewhere that's fast to look up.
# The brute force searches through the array for the complement every time.
# Searching an array means checking elements one by one — that's slow.
# But dictionaries give you instant lookups. So you trade memory (storing values in a dictionary) for speed (finding them in O(1) instead of scanning).

# # Slow: searching an array → check one by one
# if complement in nums:  # scans the whole list

# # Fast: searching a dictionary → jumps straight to it
# if complement in seen:  # instant lookup

# Why is a dictionary lookup instant?
# A dictionary uses something called a hash function.
# It takes your key (like the number 7), runs a calculation on it, and gets back a memory address where the value is stored.
# It doesn't search — it calculates where to look. Like knowing the exact shelf number in a warehouse versus walking every aisle.
# When you'll see this pattern again:
#     almost everywhere. Caching, memoization, frequency counting, deduplication — they're all "store something now so you can find it fast later."


# PATTERN 3: The Complement Pattern
# The key insight in Two Sum isn't the dictionary — it's what you look up.
# Instead of asking "do any two numbers add to target?", you reframe it:
# For each number, does target - num already exist?
# That's the complement.
# You turned a two-variable problem ("find a and b where a + b = target") into a one-variable problem ("for this a, does b exist?").
# complement = target - num  # what WOULD complete the pair?
# if complement in seen:     # have I seen that number before?
# When you'll see this again:
# any problem asking you to find pairs or groups that satisfy some equation.
# If the equation is a + b = something, the complement of a is something - a.
# If it's a * b = something, the complement is something / a. The shape changes, the pattern doesn't.


# PATTERN 4: "Have I Seen This Before?" (Single-Pass Hash Map)
# Your solution doesn't just use a dictionary — it builds the dictionary as it goes.
# This is a specific pattern called a single-pass hash map. Here's the timeline of what happens:
# Notice: you never need a second pass.
# You don't build the whole dictionary first and then search.
# You check and store in the same loop.
# This works because when you find a match, both numbers have already been encountered — one now, one earlier.
# Mental model: think of it like walking through a crowd looking for your partner for a dance.
# Each person you pass, you ask "is my partner already standing in the waiting area?"
# If no, you step into the waiting area yourself. If yes, you've found your pair.


# Big O: the core idea
# Big O describes the growth rate. It answers: "if I double the input size, what happens to the work?"
# Think of it with a real scenario. You have a list of 100 names:

# O(1) — constant: looking up a key in a dictionary. Whether you have 100 names or 10 million, one calculation finds it. Doubling input changes nothing.
# O(n) — linear: scanning a list once. 100 names → 100 checks. 200 names → 200 checks. Double input, double work. Your hash map solution does this — one pass through the array.
# O(n²) — quadratic: the brute force nested loop. 100 names → 10,000 pair checks. 200 names → 40,000 pair checks. Double input, quadruple work. This is why it's slow — it doesn't just get worse, it gets worse fast.

# Your solution's complexity:
# What	        Why
# Time	O(n)	One loop through the array. Dictionary lookup inside the loop is O(1). So n iterations × O(1) work each = O(n) total.
# Space	O(n)	In the worst case, you store almost every number in seen before finding the pair. n numbers → dictionary of up to n entries.

# The brute force is O(n²) time but O(1) space — it uses no extra storage. Your solution flips that tradeoff: faster time, more space. That's the "trade space for time" pattern in action.


# HOW TO RECOGNIZE THESE PATTERNS IN FUTURE PROBLEMS
# Here's a cheat sheet you can internalize, not memorize:
# "Find a pair that satisfies X" → think complement + hash map. Two Sum, Two Sum II, pairs with a given difference — same skeleton.
# "How many times does each thing appear?" → frequency counter with a dictionary. Same tool, different use.
# "Have I seen this before?" → set or dictionary. Detecting duplicates, finding first repeats, checking membership.
# "I'm doing a nested loop and the inner loop is just searching" → that inner loop can probably be replaced by a dictionary or a set.
# "Can I do better than O(n²)?" → almost always means either sorting (O(n log n)) or hashing (O(n)). Those are your two main escape routes from nested loops.


def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


print(twoSum([5, 5], 10))
