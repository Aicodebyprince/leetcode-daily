# Triangle - Minimum Path Sum

## Problem
Given a triangle of numbers, find the minimum path sum from top to bottom.

At each step, you can move to adjacent numbers in the next row.

---

## Approach
I used a bottom-up dynamic programming approach.

Starting from the last row, I keep updating a DP array where each value represents the minimum path sum from that position to the bottom.

This avoids recomputation and uses only one extra array.

---

## Example

**Input:**
[[2],
[3,4],
[6,5,7],
[4,1,8,3]]


**Output:**
11


---

## Complexity
- Time Complexity: O(n²)
- Space Complexity: O(n)

---

## Key Learning
Bottom-up dynamic programming helps solve path problems efficiently using minimal extra space.
