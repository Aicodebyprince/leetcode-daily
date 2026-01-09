# Merge Sorted Array

## Problem
You are given two sorted arrays. The first array has extra space at the end to hold elements from the second array.

Merge both arrays into `nums1` so that it becomes one sorted array.

---

## Approach
I merge the arrays from the end instead of the beginning.

Three pointers are used:
- One for the last valid element in `nums1`
- One for the last element in `nums2`
- One for the last position in `nums1`

At each step, the larger element is placed at the end.

---

## Example

**Input:**
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3

**Output:**
[1,2,2,3,5,6]

---

## Complexity
- Time Complexity: O(m + n)
- Space Complexity: O(1)

---

## Key Learning
Merging from the back avoids overwriting elements and allows the merge to be done in-place.
