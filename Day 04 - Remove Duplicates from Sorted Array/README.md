# Remove Duplicates from Sorted Array

## Problem
Given a sorted array of integers, remove the duplicates in-place so that each unique element appears only once.

Return the number of unique elements `k`.  
The first `k` elements of the array should contain the unique values.

---

## Approach
Since the array is sorted, duplicate elements appear next to each other.

I used a two-pointer approach:
- One pointer scans the array
- The other pointer keeps track of where the next unique element should be placed

Whenever a new value is found, it is moved to the correct position.

---

## Example

**Input:**
[0,0,1,1,1,2,2,3,3,4]


**Output:**
k = 5
Array = [0,1,2,3,4,,,,,_]
---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

---
## Key Learning
Using the fact that the array is sorted allows us to remove duplicates efficiently without using extra space.
## Key Learning
Using the fact that the array is sorted allows us to remove duplicates efficiently without using extra space.
