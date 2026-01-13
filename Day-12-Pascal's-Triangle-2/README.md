# Pascal's Triangle II

## Problem
Given a row index, return that row of Pascal’s Triangle.

---

## Approach
Instead of building the entire triangle, I use a single list.

The list is updated from right to left so previous values are not lost while computing new ones.

---

## Example

**Input:**
3


**Output:**
[1,3,3,1]


---

## Complexity
- Time Complexity: O(n²)
- Space Complexity: O(n)

---

## Key Learning
Updating from right to left allows Pascal’s Triangle to be built using only one array.

