# Word Search

## Problem
Given a 2D grid of characters and a word, determine if the word exists in the grid.

The word must be formed by sequentially adjacent cells (up, down, left, right), and the same cell cannot be used more than once.

---

## Approach
I used Depth First Search (DFS) with backtracking.

For each cell in the grid, I attempt to match the word starting from that cell.
Cells are temporarily marked as visited to avoid reuse and restored after exploring each path.

If all characters of the word are matched, the function returns true.

---

## Example

**Input:**
board = [
["A","B","C","E"],
["S","F","C","S"],
["A","D","E","E"]
]
word = "ABCCED"


**Output:**
true


---

## Complexity
- Time Complexity: O(m × n × 4^k)
- Space Complexity: O(k)

---

## Key Learning
Backtracking helps explore all possible paths while undoing invalid choices efficiently.
