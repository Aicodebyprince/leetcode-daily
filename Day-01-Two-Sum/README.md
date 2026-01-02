# Two Sum
## Problem
Given an array of integers `nums` and an integer `target`, find the indices of two numbers such that their sum is equal to the target.
You can assume that there is exactly one valid answer and the same element cannot be used twice.

## Approach
While solving this problem, the first idea is to check all possible pairs, but that would be slow.

To make it efficient, I used a HashMap (dictionary) to keep track of numbers that I have already visited.

For each number in the array:
- I calculate the value needed to reach the target.
- If this required value already exists in the dictionary, I return both indices.
- Otherwise, I store the current number with its index for future checks.

This way, the problem is solved in a single pass.
## Example

**Input:**
nums = [2, 7, 11, 15]
target = 9

**Output:**
[0,1]

**Explanation:**
`nums[0] + nums[1] = 2 + 7 = 9`, which matches the target.

## Complexity Analysis
Time Complexity:O(n)  
Space Complexity:O(n)

## Key Takeaway
Using a HashMap helps reduce the time complexity from O(n²) to O(n) by avoiding unnecessary repeated 
