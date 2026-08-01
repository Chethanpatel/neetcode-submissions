class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if set(s) != set(t):
            return False

        ss, st = list(s), list(t)
        for char in s:
            if char in t:
                ss.remove(char)
                st.remove(char)


        print(s)
        print(t)
        
        return ss == st
        