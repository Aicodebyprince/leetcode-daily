# Integer to Roman

## Problem
Given an integer between 1 and 3999, convert it to a Roman numeral.

Roman numerals are formed by subtracting the largest possible values and handling special subtractive cases.

---

## Approach
I used a greedy strategy with predefined mappings of integers to Roman symbols.

By always choosing the largest valid Roman value, the number is reduced step by step until it reaches zero.

Special cases like 4, 9, 40, and 900 are handled by including them directly in the mapping.

---

## Example

**Input:**
1994


**Output:**
MCMXCIV

---

## Complexity
- Time Complexity: O(1)
- Space Complexity: O(1)

---

## Key Learning
Greedy algorithms work well when choices can be made locally to reach a correct global solution.
