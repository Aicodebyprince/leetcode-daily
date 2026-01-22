# Valid Parentheses

## Problem
Given a string containing only parentheses characters, determine if the string is valid.

A string is valid if brackets are closed in the correct order and with matching types.

---
## Approach
I used a stack to track opening brackets.

When a closing bracket is found, I check if it matches the most recent opening bracket stored in the stack.

If all brackets match correctly and the stack is empty at the end, the string is valid.

---
## Example

**Input:**
"([])"


**Output:**
true


---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)

---

## Key Learning
Stacks are ideal for problems that require matching pairs in a specific order.
