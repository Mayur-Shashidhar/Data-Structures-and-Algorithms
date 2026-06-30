# Shuffle the Array
- Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
- Return the array in the form [x1,y1,x2,y2,...,xn,yn].

---

## Approach
- Create an empty list l to store the shuffled result
- Split the input array into two halves:
    - l1 contains the first n elements (indices 0 to n-1)
    - l2 contains the last n elements (indices n to 2n-1)
- Loop through indices from 0 to n-1:
    - Append the element at index i from l1
    - Append the element at index i from l2
- This creates the pattern: x₀, y₀, x₁, y₁, x₂, y₂, ...
- Return the shuffled list


### Complexity
- Time : O(n)
- Space : O(n)

---
