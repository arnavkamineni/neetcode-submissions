from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b
        }              
        stack = deque()
        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(operators[token](a,b))
            
        return int(stack.pop())