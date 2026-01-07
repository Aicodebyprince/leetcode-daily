# Search Insert Position

## Problem
Given a sorted array of distinct integers and a target value, return the index if the target is found.

If the target is not found, return the index where it would be inserted to maintain sorted order.

---

## Approach
Because the array is sorted, I used binary search to solve the problem in O(log n) time.

I repeatedly divide the search space in half:
- If the target is found, return its index
- If not found, the left pointer gives the correct insert position

---

## Example

**Input:**
nums = [1,3,5,6], target = 2



**Output:**
1


---

## Complexity
- Time Complexity: O(log n)
- Space Complexity: O(1)

---
## Key Learning
Binary search can be used not only to find elements, but also to determine correct insertion positions efficiently.
## Key Learning
Binary search can be used not only to find elements, but also to dete
