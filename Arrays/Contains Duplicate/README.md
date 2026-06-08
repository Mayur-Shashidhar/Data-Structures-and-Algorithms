# Contains Duplocate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

---

## Approach
- Create an empty HashSet.
- Traverse the array one element at a time.
- For each element:
    - Check if the element already exists in the HashSet.
    - If it exists:
          - Duplicate found.
          - Return True.
- Otherwise:
    - Add the element to the HashSet.
    - Continue until the end of the array.
- If the traversal finishes without finding any duplicate, return False.

### Complexity
- Time : O(n)
- Space : O(n)

---
