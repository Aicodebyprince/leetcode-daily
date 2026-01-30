# Regular Expression Matching

## Problem
Given a string and a pattern containing '.' and '*', determine if the entire string matches the pattern.

'.' matches any single character  
'*' matches zero or more of the preceding character

---

## Approach
I used Dynamic Programming.

I defined dp[i][j] to represent whether the first i characters of the string match the first j characters of the pattern.

The '*' character is handled by considering:
- Zero occurrences of the previous character
- One or more occurrences if the character matches

This ensures all valid matching cases are covered efficiently.

---

## Example

**Input:**
s = "ab"
p = ".*"


**Output:**
true


---

## Complexity
- Time Complexity: O(m × n)
- Space Complexity: O(m × n)

---
## Key Learning
Dynamic programming is essential for handling overlapping subproblems in complex pattern matching.
