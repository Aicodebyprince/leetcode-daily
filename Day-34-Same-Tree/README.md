# Same Tree

## Problem
Given two binary trees, determine if they are structurally identical and have the same node values.

---
## Approach
I used recursion to compare the trees.

At each node:
- Both nodes must exist
- Their values must be equal
- Their left and right subtrees must also be equal

If any mismatch occurs, the trees are not the same.

---
## Example

**Input:**
p = [1,2,3]
q = [1,2,3]


**Output:**
true


---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)

---

## Key Learning
Recursive traversal is effective for comparing tree structure and values.
