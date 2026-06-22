class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position, speed))
        stack = []

        for pos, spd in reversed(cars):
            time = float(target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)
