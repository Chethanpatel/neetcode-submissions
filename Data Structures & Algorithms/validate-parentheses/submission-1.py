class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)%2 == 1:
            return False

        map = {
            ')':'(',
            '}':'{',
            ']':'['
        }       
        
        stack = list()

        for char in s:
            if char in map.values():
                stack.append(char)
            else:
                if map.get(char) == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return True
                    