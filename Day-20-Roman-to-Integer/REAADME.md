# Roman to Integer

## Problem
Given a Roman numeral string, convert it into an integer.

Roman numerals usually add values from left to right, but subtraction is used when a smaller value comes before a larger one.

---

## Approach
I used a dictionary to map Roman symbols to their integer values.

While iterating through the string:
- If the current symbol is smaller than the next one, I subtract it
- Otherwise, I add it to the total

This handles all subtraction cases correctly.

---

## Example

**Input:**
"MCMXCIV"


**Output:**
1994


---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Key Learning
Comparing the current and next symbols makes it easy to handle Roman numeral subtraction rules.
