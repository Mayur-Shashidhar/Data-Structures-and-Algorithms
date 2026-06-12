# Koko Eating Bananas
- Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
- Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
- Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
- Return the minimum integer k such that she can eat all the bananas within h hours.

---

## Approach
- The minimum possible speed is: 1 banana/hour
- The maximum possible speed is: max(piles) bananas/hour
- Use Binary Search on this speed range.
- Pick a middle speed.
- Calculate how many hours Koko would need at that speed.
- If Koko can finish within h hours:
    - This speed is a possible answer.
    - Try to find a smaller valid speed.
- If Koko cannot finish within h hours:
    - The speed is too slow.
    - Try a larger speed.
- Continue until the search space becomes empty.
- Return the smallest speed that works.


### Complexity
- Time : O(n log m)
- Space : O(1)

---
