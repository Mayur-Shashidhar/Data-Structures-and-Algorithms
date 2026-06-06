# Best Time to Buy and Sell Stock
- You are given an array prices where prices[i] is the price of a given stock on the ith day.
- You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
- Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

---

## Approach: Running Minimum (Greedy)
- Maintain two variables:
    - min_price: Stores the lowest stock price encountered so far.
    - max_profit: Stores the highest profit found so far.

### Algorithm
- Initialize:
    - min_price as the first price.
    - max_profit as 0.
- Traverse the array from left to right.
- For each price:
    - Update min_price if a lower price is found.
    - Calculate the profit if sold today.
    - Update max_profit if this profit is larger.
- Return max_profit.

### Complexity
- Time : O(n)
- Space : O(1)

---
