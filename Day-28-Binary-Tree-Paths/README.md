# Binary Tree Paths

## Problem
Given a binary tree, return all root-to-leaf paths.

A path is defined as a sequence of node values from the root node to a leaf node.

---
## Approach
I used Depth First Search (DFS).

Starting from the root, I build the path as a string.
When a leaf node is reached, the current path is added to the result list.

DFS naturally explores all root-to-leaf paths.
---

## Example

**Input:**
[1,2,3,null,5]


**Output:**
["1->2->5", "1->3"]


---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)

---

## Key Learning
DFS is well-suited for problems that require exploring complete paths in a tree.
