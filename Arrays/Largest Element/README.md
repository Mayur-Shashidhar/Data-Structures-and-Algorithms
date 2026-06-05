# Largest Element
Given an array of integer nums, return the value of the largest element in the array.

---

## Brute Force
- Sort the array in the ascending array.
- Print the element at the [ size of the array - 1 ]th index, which coresponds to the largest element in the array.

### Complexity
- Time : O(n log n)
- Space : O(n)

---

## Optimal Approach
- Create a variable called largest and initialize it with the value of the first element in the array.
- Use a loop to iterate through the rest of the elements of the array.
- In each iteration, compare the current element with the largest variable.
- If the current element is greater than the largest value, update the largest value with the current element's value.
- After completing the loop, print the largest variable, which will hold the largest value in the array.

### Complexity
- Time : O(n)
- Space : O(1)

---
