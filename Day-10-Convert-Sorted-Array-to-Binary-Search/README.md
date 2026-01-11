# Convert Sorted Array to Binary Search Tree

## Problem
Given a sorted array, convert it into a height-balanced Binary Search Tree.

---

## Approach
To make the tree balanced, I choose the middle element of the array as the root.

The left half of the array is used to build the left subtree and the right half is used to build the right subtree.

This process is repeated recursively until the tree is built.

---

## Example

**Input:**
[-10, -3, 0, 5, 9]


**Output:**
A height-balanced BST with 0 as the root


---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)

---

## Key Learning
Using the middle element helps keep the tree balanced and satisfies the BST property.
