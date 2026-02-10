# Best Time to Buy and Sell Stock II

## Problem
Given an array of stock prices, find the maximum profit by making as many buy and sell transactions as you like, while holding at most one stock at a time.

---

## Approach
I used a greedy approach.

Whenever the price increases from one day to the next, I add the difference to the total profit. This captures all profitable opportunities without missing any future gains.

---

## Example

**Input:**
[7,1,5,3,6,4]


**Output:**
7


---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Key Learning
Summing all upward price movements yields the maximum profit when multiple transactions are allowed.
