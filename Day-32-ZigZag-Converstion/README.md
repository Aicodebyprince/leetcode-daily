# Zigzag Conversion

## Problem
Given a string and a number of rows, write the string in a zigzag pattern and read it row by row.

---

## Approach
I simulated the zigzag pattern using a list of strings.

Each character is added to the current row, and the direction changes when the top or bottom row is reached.

Finally, all rows are joined to form the result.

---

## Example

**Input:**
s = "PAYPALISHIRING"
numRows = 3


**Output:**
"PAHNAPLSIIGYIR"

---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)

---

## Key Learning
Pattern problems can often be solved by simulation instead of building complex data structures.
