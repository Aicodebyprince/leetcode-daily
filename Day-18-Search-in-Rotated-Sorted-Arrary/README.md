# Search in Rotated Sorted Array

## Problem
Given a sorted array that is possibly rotated, find the index of a target value using O(log n) time.

If the target does not exist, return -1.

---

## Approach
I used a modified binary search.

At each step, one half of the array is guaranteed to be sorted.  
By checking which half is sorted, I can decide whether the target lies in that half or the other.

This allows binary search to work even with rotation.

---

## Example

**Input:**
nums = [4,5,6,7,0,1,2]
target = 0


**Output:**
4

---

## Complexity
- Time Complexity: O(log n)
- Space Complexity: O(1)

---

## Key Learning
Even in a rotated array, binary search works if we correctly identify the sorted half.
