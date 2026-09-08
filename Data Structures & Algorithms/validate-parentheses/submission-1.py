class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0]

        for c in s:
            if c == ')':
                last = stack.pop()
                if last != '(':
                    return False
            elif c == ']':
                last = stack.pop()
                if last != '[':
                    return False
            elif c == '}':
                last = stack.pop()
                if last != '{':
                    return False
            else:
                stack.append(c)
        
        if stack != [0]:
            return False
        else:
            return True
