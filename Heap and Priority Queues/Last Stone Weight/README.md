# Last Stone Weight
- You are given an array of integers stones where stones[i] is the weight of the ith stone.
- We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
    - If x == y, both stones are destroyed, and
    - If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
- At the end of the game, there is at most one stone left.
- Return the weight of the last remaining stone. If there are no stones left, return 0.

---

## Approach
- Convert all stone weights to negative values.
- Heapify the array.
- While more than one stone remains:
    - Pop the two largest stones.
    - If they are different:
        - Push back their difference.
- Return the remaining stone.
- If the heap becomes empty: Return 0


### Complexity
- Time : O(n log n)
- Space : O(n)

---
