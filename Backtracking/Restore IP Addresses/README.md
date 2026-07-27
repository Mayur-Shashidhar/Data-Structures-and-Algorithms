# Restore IP Addresses
- A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
    - For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
- Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

## Approach
- Start from index 0.
- Try segments of length:
  -  1
  -  2
  -  3
- Validate the segment.
- If valid: Add to current path.
- Recurse from the next index.
- Undo.
- Store only if exactly 4 parts are formed.


### Complexity
- Time : O(1)
- Space : O(1)

---
