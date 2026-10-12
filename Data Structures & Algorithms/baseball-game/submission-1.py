class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]

        for i in range(len(operations)):
            if operations[i] == '+':
                res.append(int(res[-1])+int(res[-2]))
            elif operations[i] == 'D':
                res.append(2*int(res[-1]))
            elif operations[i] == 'C':
                res.pop()
            else:
                res.append(int(operations[i]))
        x=0
        for i in res:
            x+=i
        return x


