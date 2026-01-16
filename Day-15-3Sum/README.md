# 3Sum

## Problem
Given an integer array, find all unique triplets such that the sum of the three numbers is zero.

The solution should not contain duplicate triplets.

---

## Approach
I first sorted the array to make duplicate handling easier.

For each element, I fixed it as the first number and used a two-pointer approach to find the remaining two numbers whose sum equals the negative of the fixed value.

Duplicates are skipped carefully to ensure only unique triplets are added.

---

## Example

**Input:**
[-1,0,1,2,-1,-4]


**Output:**
[[-1,-1,2], [-1,0,1]]



---

## Complexity
- Time Complexity: O(n²)
- Space Complexity: O(1)

---

## Key Learning
Sorting combined with the two-pointer technique helps efficiently solve multi-sum problems while avoiding duplicates.
