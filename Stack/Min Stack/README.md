# Min Stack
- Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
- Implement the MinStack class:
    - MinStack() initializes the stack object.
    - void push(int value) pushes the element value onto the stack.
    - void pop() removes the element on the top of the stack.
    - int top() gets the top element of the stack.
    - int getMin() retrieves the minimum element in the stack.
- You must implement a solution with O(1) time complexity for each function.

---

## Approach
- Create a normal stack to store all values.
- Create a second stack to store the minimum value at each position.
- For every push operation:
    - Push the value into the normal stack.
    - Push the minimum of:
        - current value
        - current minimum into the min stack.
- For every pop operation: Remove the top element from both stacks.
- For top(): Return the top of the normal stack.
- For getMin(): Return the top of the min stack.


### Complexity
- push()   : O(1)
- pop()    : O(1)
- top()    : O(1)
- getMin() : O(1)

---
