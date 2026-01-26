# Isomorphic Strings

## Problem
Given two strings, determine if they are isomorphic.

Two strings are isomorphic if characters in one string can be replaced to get the other string, with a one-to-one mapping.

---

## Approach
I used two hash maps to track character mappings in both directions.

One map stores the mapping from the first string to the second, and the other ensures that no two characters map to the same character.

If a conflict is found, the strings are not isomorphic.

---

## Example

**Input:**
s = "egg"
t = "add"


**Output:**
true


---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)

---

## Key Learning
Using two mappings ensures a consistent and one-to-one character replacement.
