# Find the Index of the First Occurrence in a String

## Problem
Given two strings `haystack` and `needle`, find the index of the first occurrence of `needle` in `haystack`.

Return -1 if `needle` is not found.

---

## Approach
I used a sliding window approach.

For each possible starting index in `haystack`, I compared the substring of length equal to `needle` with the `needle`.

The first index where they match is returned.

---

## Example

**Input:**
haystack = "sadbutsad"
needle = "sad"


**Output:**
0

---

## Complexity
- Time Complexity: O((n − m) × m)
- Space Complexity: O(1)

---

## Key Learning
Simple substring comparison works efficiently for basic string search problems.

