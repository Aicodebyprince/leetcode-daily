# 3Sum Closest

## Problem
Given an integer array and a target value, find the sum of three integers that is closest to the target.

You can assume there is exactly one solution.

---

## Approach
I first sorted the array.

Then, for each element, I fixed it as the first number and used two pointers to find the best possible pair that gives a sum closest to the target.

At each step, I compared the current sum with the closest sum found so far and updated it when necessary.

---

## Example

**Input:**
nums = [-1,2,1,-4]
target = 1


**Output:**
2

---

## Complexity
- Time Complexity: O(n²)
- Space Complexity: O(1)

---

## Key Learning
Sorting combined with the two-pointer technique helps efficiently solve closest-sum problems.
