from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        pairs = { "(":")", '[':']', '{':'}' }
        for char in s:
            print(char)
            if char in pairs.keys():
                stack.append(char)
                
            else:
                if len(stack) == 0:
                    return False
                if pairs[stack.pop()] != char:
                    return False

        return len(stack) == 0

        