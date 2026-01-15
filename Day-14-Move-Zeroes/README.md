# Move Zeroes


## Problem
Move all zeros in the array to the end while keeping the order of non-zero elements.

The operation must be done in-place.


---

## Approach
I used a two-pointer method.

One pointer scans the array and the other keeps track of where the next non-zero element should be placed.  
This keeps non-zero values in order and moves zeros to the end.

---

## Example

**Input:**
[0,1,0,3,12]

**Output:**
[1,3,12,0,0]

---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Key Learning
Two pointers help rearrange elements in-place without using extra memory.
