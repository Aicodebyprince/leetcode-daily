# Add Binary

## Problem
Given two binary strings, return their sum as a binary string.

---

## Approach
I used a two-pointer approach starting from the end of both strings.

At each step, I added the digits along with a carry and stored the result bit.
The carry is updated just like normal binary addition.

Finally, the result is reversed to get the correct order.

---

## Example

**Input:**
a = "1010"
b = "1011"


**Output:**
"10101"

---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(n)

---

## Key Learning
Binary addition follows the same logic as decimal addition, with base-2 rules.
