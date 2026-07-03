# Top K Frequent Words
- Given an array of strings words and an integer k, return the k most frequent strings.
- Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

---

## Approach
- Count the frequency of each word.
- Store each word with its frequency.
- Sort by:
    - Frequency in descending order.
    - Alphabetical order if frequencies are equal.
- Return the first k words.


### Complexity
- Time : O(n log n)
- Space : O(n)

---
