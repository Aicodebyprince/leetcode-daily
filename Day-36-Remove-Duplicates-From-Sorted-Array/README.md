# Remove Duplicates from Sorted Array II

## Problem
Given a sorted array, remove duplicates in-place such that each element appears at most twice.

Return the number of valid elements after modification.

---

## Approach
Since the array is sorted, duplicates appear consecutively.

I used a two-pointer approach:
- The first two elements are always valid.
- From the third element onward, a number is kept only if it differs from the element two positions before.

This ensures no element appears more than twice.

---

## Example

**Input:**
[1,1,1,2,2,3]


**Output:**
k = 5
nums = [1,1,2,2,3,_]


---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Key Learning
Checking against the element two positions back is an elegant way to control duplicate frequency.
