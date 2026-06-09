# Majority Element
- Given an array nums of size n, return the majority element.
- The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

---

## Approach 1: Brute Force

For every element:

1. Count how many times it appears in the entire array.
2. If the count is greater than `n/2`, return that element.


## Algorithm

For each element:
- Select: current = nums[i]
- Traverse the entire array and count occurrences.
- If: count > n/2, return the current element.


### Complexity
- Time : O(n²)
- Space : O(1)


---

## Approach 2: HashMap (Frequency Counting)

Store the frequency of every element in a frequency table.
The element whose frequency exceeds n/2 is the answer.


## Algorithm
- Create an empty HashMap.
- Traverse the array and store frequencies.
- Traverse the HashMap.
- Return the element whose frequency is greater than n/2


### Complexity
- Time : O(n)
- Space : O(n)

---

## Approach 3: Boyer-Moore Voting Algorithm (Optimal)
- The majority element appears more than half the time.
- Therefore, even if every non-majority element cancels one occurrence of the majority element, the majority element will still remain.


## Voting Concept
- Maintain:
    - candidate
    - count


Rules:
- If count becomes 0: Choose the current element as the new candidate.
- If current element equals candidate: count += 1
- Otherwise: count -= 1
- This simulates cancelling votes between different elements.


## Complexity 
- Time : O(n)
- Space Complexity : O(1)

---
