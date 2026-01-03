
# Longest Common Prefix

## Problem
Given an array of strings, find the longest common prefix shared by all strings.

If there is no common prefix, return an empty string `""`.

---

## Approach
To solve this problem, I assumed the first string as the initial prefix because the longest possible prefix cannot be longer than it.

Then, I compared this prefix with each remaining string:
- If a string does not start with the current prefix, I shorten the prefix by removing the last character.
- I keep reducing the prefix until it matches the start of the current string.
- If the prefix becomes empty at any point, it means there is no common prefix.

After checking all strings, the remaining prefix is the longest common prefix.

---

## Example

**Input:**
["flower", "flow", "flight"]


**Output:**
"fl"

**Explanation:**
All strings start with `"fl"`, but they differ after that, so `"fl"` is the longest common prefix.

---

## Complexity
- **Time Complexity:** O(n × m)  
  where `n` is the number of strings and `m` is the length of the prefix.
- **Space Complexity:** O(1)

---

## Key Learning
By gradually reducing the prefix and stopping early when a mismatch occurs, we can efficiently find the 
