# Best Time to Buy and Sell Stock

## Problem
Given an array of stock prices, find the maximum profit that can be achieved by buying once and selling once in the future.

Return 0 if no profit is possible.

---

## Approach
I used a greedy one-pass approach.

While iterating through the prices:
- I track the minimum price seen so far
- At each step, I calculate the profit if sold on that day
- The maximum profit is updated accordingly

---

## Example

**Input:**
[7,1,5,3,6,4]


**Output:**
5

---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Key Learning
Tracking the minimum value so far allows optimal decisions in a single pass.
