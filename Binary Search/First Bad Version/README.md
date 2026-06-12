# First Bad Version
- You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
- Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
- You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

---

## Approach
- Search between version: 1 to n
- Pick the middle version.
- Check whether it is bad using: isBadVersion(mid)
- If the version is good:
    - The first bad version must be after it.
    - Search the right half.
- If the version is bad:
    - It could be the first bad version.
    - Store it as a possible answer.
    - Search the left half to see if there is an earlier bad version.
- Continue until the search space becomes empty.
- Return the stored answer.


### Complexity
- Time : O(log n)
- Space : o(1)

---
