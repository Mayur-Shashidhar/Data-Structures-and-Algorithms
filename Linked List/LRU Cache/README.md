# LRU Cache
- Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
- Implement the LRUCache class:
    - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
    - int get(int key) Return the value of the key if the key exists, otherwise return -1.
    - void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
- The functions get and put must each run in O(1) average time complexity.

---

## Approach
- Use a HashMap to store key-to-node mappings.
- Use a Doubly Linked List to maintain usage order.
- Whenever a key is accessed using get():
    - Move that node to the most recently used position.
- Whenever a key is inserted using put():
    - If the key already exists, update its value and move it to the most recently used position.
- If the cache is full:
    - Remove the least recently used node from the linked list.
    - Remove it from the HashMap.
- Insert the new node as the most recently used node.
- Return values in O(1) time.


### Complexity
- get() : O(1)
- put() : O(1)
- Space : O(capacity)

---
