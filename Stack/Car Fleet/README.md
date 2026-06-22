# Car Fleet
- There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
- You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.
- A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
- A car fleet is a single car or a group of cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.
- If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
- Return the number of car fleets that will arrive at the destination.

---

## Approach
- Pair each car's position and speed.
- Sort cars by position in ascending order.
- Traverse cars from right to left.
- Compute the time required for each car to reach the target.
- Maintain a stack of fleet arrival times.
- If the current car takes longer than the fleet ahead:
    - It forms a new fleet.
    - Push its time onto the stack.
- Otherwise:
    - It joins the fleet ahead.
    - Do not create a new fleet.
- After processing all cars, the number of fleet times in the stack is the answer.


### Complexity
- Time : O(n log n)
- Space : O(n)

---
