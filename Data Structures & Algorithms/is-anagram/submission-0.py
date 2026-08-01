class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ss, st = list(s), list(t)
        for char in s:
            if char in t:
                st.remove(char)
                ss.remove(char)


        print(s)
        print(t)
        
        return ss == st
        