# Guess Number Higher or Lower
- We are playing the Guess Game. The game is as follows:
- I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).
- Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
- You call a pre-defined API int guess(int num), which returns three possible results:
    - -1: Your guess is higher than the number I picked (i.e. num > pick).
    = 1: Your guess is lower than the number I picked (i.e. num < pick).
    - 0: your guess is equal to the number I picked (i.e. num == pick).
- Return the number that I picked.

---

## Approach
- Search between: 1 and n
- Pick the middle number.
- Call: guess(mid)
- If: 0, return mid.
- If: 1, the hidden number is larger. Search right half.
- If: -1, the hidden number is smaller. Search left half.
- Continue until found.


### Complexity
- Time : O(log n)
- Space : O(1)

---
