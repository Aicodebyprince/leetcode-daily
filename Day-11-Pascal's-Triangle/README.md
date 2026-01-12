# Pascal's Triangle

## Problem
Given a number `numRows`, generate the first `numRows` of Pascal’s triangle.

---

## Approach
Each row of Pascal’s triangle is built from the previous row.

The first and last values of every row are always 1.  
The middle values are the sum of the two values above them from the previous row.

---

## Example

**Input:**
5

**Output:**
[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

---

## Complexity
- Time Complexity: O(n²)
- Space Complexity: O(n²)

---

## Key Learning
Pascal’s triangle can be built row by row using values from the previous row.
