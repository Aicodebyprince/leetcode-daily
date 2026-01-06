# Remove Element

## Problem
Given an integer array and a value `val`, remove all occurrences of `val` in-place.

Return the number of elements that are not equal to `val`.  
The first `k` elements of the array should contain the valid values.

---

## Approach
I used a two-pointer approach.

One pointer scans the array, and another pointer keeps track of where the next valid element should be placed.  
Whenever an element is not equal to `val`, it is moved to the front of the array.

The order of elements does not matter.

---

## Example

**Input:**
nums = [3,2,2,3], val = 3


**Output:**
k = 2
nums = [2,2,,]

---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Key Learning
Using in-place modification with two pointers allows us to remove elements efficiently without extra space.
