# Add Two Numbers

## Problem
You are given two non-empty linked lists that represent two non-negative integers.  
The digits are stored in reverse order, and each node contains a single digit.

The task is to add the two numbers and return the sum as a linked list in the same reverse order.

---

## Approach
This problem is similar to adding two numbers digit by digit.

Since the digits are already in reverse order, we can start from the head of both linked lists and add corresponding digits directly.

I used a dummy node to build the result linked list easily and a `carry` variable to handle values greater than 9.

For each step:
- Take the value from both lists (use 0 if a list ends)
- Add them along with the carry
- Store the last digit in a new node
- Move to the next nodes

The process continues until both lists and the carry are fully processed.

---

## Example

**Input:**
l1 = [2,4,3]
l2 = [5,6,4]

**Output:**
[7,0,8]


**Explanation:**
The numbers represented are 342 and 465.  
Their sum is 807, which is returned as a linked list `[7,0,8]`.

---

## Complexity
- **Time Complexity:** O(n)  
- **Space Complexity:** O(n)  

Here, `n` is the length of the longer linked list.

---

## Key Learning
Using a dummy node simplifies linked list construction, and maintaining a carry helps handle digit 
