# Length of Last Word

## Problem
Given a string consisting of words and spaces, return the length of the last word.

A word is defined as a sequence of non-space characters.

---

## Approach
I scanned the string from the end.

First, I skipped any trailing spaces.  
Then, I counted the characters until a space was found.

This directly gives the length of the last word without using extra space.

---

## Example

**Input:**
"Hello World"


**Output:**
5

---

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

---

## Key Learning
Scanning from the end helps handle trailing spaces efficiently.
