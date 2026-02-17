# Is Subsequence

## Problem
Given two strings s and t, return true if s is a subsequence of t.

A subsequence maintains relative character order but does not require contiguous characters.

---

## Approach
I used a two-pointer approach.

One pointer iterates over s and the other over t.
Whenever characters match, I move the pointer of s.
If all characters of s are matched, it is a subsequence.

---

## Example

**Input:**
s = "abc"
t = "ahbgdc"


**Output:**
true


---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Key Learning
Two-pointer technique is efficient for subsequence checking problems.

