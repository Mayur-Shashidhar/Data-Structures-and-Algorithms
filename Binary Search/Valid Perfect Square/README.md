# Valid Perfect Square
- Given a positive integer num, return true if num is a perfect square or false otherwise.
- A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
- You must not use any built-in library function, such as sqrt.

---

## Approach
- The possible square root must lie between: 1 and num
- Use Binary Search on this range.
- Pick the middle number.
- Calculate: mid × mid
- If: mid² == num, Return: True because we found an integer square root.
- If: mid² < num
    - The square root must be larger.
    - Search the right half.
- If: mid² > num
    - The square root must be smaller.
    - Search the left half.
- If Binary Search finishes without finding an exact square: Return False


### Complexity
- Time : O(log n)
- Space : O(1)

---
