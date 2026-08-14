class Solution:
    def isValid(self, s: str) -> bool:
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
                    