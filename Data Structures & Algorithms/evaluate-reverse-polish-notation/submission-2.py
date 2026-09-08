class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        operators = ("+", "-", "*", "/")

        for t in tokens:
            if t in operators:
                m = stack.pop()
                n = stack.pop()
                if t == "+": val = n + m
                elif t == "-": val = n - m
                elif t == "*": val = n * m
                elif t == "/": val = int(n / m)
                stack.append(val)
            else:
                stack.append(int(t))
        
        return stack[0]
