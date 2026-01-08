# Plus One

## Problem
Given an integer represented as an array of digits, increment the number by one and return the resulting array.

The digits are stored from most significant to least significant.

---

## Approach
I start from the last digit and simulate normal addition.

- If a digit is less than 9, I add 1 and return the array.
- If a digit is 9, I set it to 0 and continue moving left.
- If all digits are 9, I add a new digit `1` at the beginning.

This approach avoids converting the array into an integer.

---

## Example

**Input:**
digits = [9,9,9]

**Output:**
[1,0,0,0]

---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Key Learning
Handling carry properly allows us to solve number-based problems directly using arrays.
