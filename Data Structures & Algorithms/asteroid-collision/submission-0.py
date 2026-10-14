class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            while stack and i<0 and stack[-1]>0:
                dif = i + stack[-1]
                if dif < 0:
                    stack.pop()
                elif dif > 0:
                    i = 0
                else:
                    i=0
                    stack.pop()
            if i:
                stack.append(i)
        return stack