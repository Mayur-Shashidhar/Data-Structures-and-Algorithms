## Sqrt(x)
- Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
- You must not use any built-in exponent function or operator.
    - For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.



## Approach 1: Binary Search
1. Search between 0 and x.
2. Calculate the middle value.
3. If: mid² == x, then return mid.
4. If: mid² < x, then:
    - mid is a valid answer.
    - Store it.
    - Try to find a larger valid answer on the right side.
5. If: mid² > x, then:
    - mid is too large.
    - Search on the left side.
6. Continue until the search space becomes empty.
7. Return the last valid answer.


### Complexity
- Time  : O(log x)
- Space : O(1)

---

# Approach 2: Newton-Raphson Method
1. Initialize: r = x
2. While: r² > x, update: r = (r + x/r) / 2
3. Continue until the approximation becomes good enough.
4. Return the integer part of `r`.


### Complexity
- Time  : O(log log x)
- Space : O(1)

---
