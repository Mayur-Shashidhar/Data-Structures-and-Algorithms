# Asteroid Collision
- We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.
- For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
- Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

---

## Approach
- Create an empty stack.
- Traverse each asteroid.
- If the asteroid is moving right:
    - Push it onto the stack.
- If the asteroid is moving left:
    - Check for collisions with right-moving asteroids on the top of the stack.
- While a collision is possible:
    - If the top asteroid is smaller, remove it.
    - If both are equal, remove both and stop processing the current asteroid.
    - If the top asteroid is larger, destroy the current asteroid.
- If the current asteroid survives all collisions, push it onto the stack.
- After processing all asteroids, return the stack.


### Complexity
- Time : O(n)
- Space : O(n)

---
