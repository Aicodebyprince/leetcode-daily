# Rotate Array

## Problem
Given an array, rotate it to the right by k steps.

The rotation must be done in-place using O(1) extra space.
---

## Approach
I used the reverse array technique.

The idea is to:
1. Reverse the entire array
2. Reverse the first k elements
3. Reverse the remaining elements

This achieves the rotation efficiently without extra memory.
---

## Example

**Input:**
nums = [1,2,3,4,5,6,7]
k = 3

**Output:**
[5,6,7,1,2,3,4]


---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Key Learning
Reversing parts of an array can help perform rotations efficiently in-place.
