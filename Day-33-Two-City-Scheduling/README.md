# Two City Scheduling

## Problem
Given the cost of flying each person to two cities, assign exactly half the people to each city with minimum total cost.
---

## Approach
I used a greedy strategy.

For each person, I calculated the difference between the cost of going to city A and city B.
After sorting by this difference, the first half are sent to city A and the remaining half to city B.

This ensures the overall minimum cost.

---
## Example

**Input:**
[[10,20],[30,200],[400,50],[30,20]]


**Output:**
110


---

## Complexity
- Time Complexity: O(n log n)
- Space Complexity: O(1)

---

## Key Learning
Sorting by cost difference allows optimal greedy assignment in scheduling problems.
