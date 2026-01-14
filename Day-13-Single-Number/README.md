# Single Number

## Problem
In an array, every element appears twice except for one.  
Find the number that appears only once.

---

## Approach
I used the XOR operation.

XOR cancels out duplicate numbers because:
- a ^ a = 0
- a ^ 0 = a

So when all numbers are XORed together, only the single number remains.

---

## Example

**Input:**
[4,1,2,1,2]

**Output:**
4

---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Key Learning
XOR is useful for finding unique elements when all others appear in pairs.
