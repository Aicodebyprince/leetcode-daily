# Valid Palindrome

## Problem
Given a string, determine if it is a palindrome after converting all letters to lowercase and removing non-alphanumeric characters.

---

## Approach
I used a two-pointer approach.

One pointer starts from the beginning and the other from the end.  
Non-alphanumeric characters are skipped, and valid characters are compared after converting them to lowercase.

If all characters match, the string is a palindrome.

---

## Example

**Input:**
"A man, a plan, a canal: Panama"


**Output:**
true

---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Key Learning
Two pointers are effective for palindrome checks when ignoring characters and case.
