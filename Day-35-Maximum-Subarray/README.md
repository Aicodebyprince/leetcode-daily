# Maximum Subarray

## Problem
Given an integer array, find the contiguous subarray with the largest sum and return that sum.

---

## Approach
I used Kadane’s Algorithm.

At each element, I decide whether to start a new subarray or continue the existing one by comparing the current value with the sum including the previous subarray.

The maximum sum encountered during the traversal is the answer.

---

## Example

**Input:**
[-2,1,-3,4,-1,2,1,-5,4]


**Output:**
6
---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Key Learning
Kadane’s Algorithm efficiently finds the maximum subarray sum in a single pass.
