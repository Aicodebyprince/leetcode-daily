# Container With Most Water

## Problem
Given an array of heights, each value represents a vertical line.  
Choose two lines that together form a container holding the maximum amount of water.

---

## Approach
I used a two-pointer approach.

One pointer starts from the left and the other from the right.  
At each step, the area is calculated using the distance between the pointers and the smaller of the two heights.

To improve the result, I move the pointer with the smaller height because the water level is limited by it.

---

## Example

**Input:**
[1,8,6,2,5,4,8,3,7]

**Output:**
49

---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

---
## Key Learning
Moving the smaller height pointer helps find a better container efficiently without checking all pairs.
## Key Learning
Moving the smaller height pointer helps find a better container efficiently without checking all p
