def dailyTemperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []  # indices, temperatures decrease

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            previous = stack.pop()
            result[previous] = i - previous

        stack.append(i)

    return result