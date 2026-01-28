# Basic Calculator

## Problem
Given a string representing a valid mathematical expression containing '+', '-', parentheses, and spaces, evaluate and return the result.

Using built-in evaluation functions is not allowed.

---

## Approach
I processed the string from left to right using a stack.

- Numbers are built digit by digit.
- The current result and sign are updated when operators appear.
- When encountering '(' the current result and sign are saved on the stack.
- When encountering ')' the sub-expression result is combined with the previous context.

This allows correct evaluation of nested expressions.

---

## Example

**Input:**
"(1+(4+5+2)-3)+(6+8)"


**Output:**
23


---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)

---

## Key Learning
Stack-based evaluation helps handle parentheses and sign changes efficiently in expression parsing.
