# Majority Element

## Problem
Given an array of integers, find the element that appears more than ⌊n / 2⌋ times.

It is guaranteed that the majority element always exists.

---

## Approach
I used the Boyer–Moore Voting Algorithm.

The idea is that the majority element appears more than half the time, so it cannot be fully canceled out by other elements.

By increasing the count for matching elements and decreasing it for different ones, the final candidate will be the majority element.

---

## Example

**Input:**
[2,2,1,1,1,2,2]


**Output:**
2

---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Key Learning
The Boyer–Moore Voting Algorithm finds the majority element efficiently without using extra space.
