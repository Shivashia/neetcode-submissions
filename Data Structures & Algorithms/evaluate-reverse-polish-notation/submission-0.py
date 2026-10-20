class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stck = []

        for i in tokens:
            if i in ['+', '-', '*', '/']:
                b = stck.pop()
                a = stck.pop()

                if i == '+':
                    res = a + b
                elif i == '-':
                    res = a - b
                elif i == '*':
                    res = a * b
                else:
                    res = int(a / b)

                stck.append(res)
            else:
                stck.append(int(i))

        return stck.pop()