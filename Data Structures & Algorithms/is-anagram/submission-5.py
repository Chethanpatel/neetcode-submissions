class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counterS, counterT = dict(), dict()

        for char in s:
            counterS[char] = 1+counterS.get(char, 0)

        for char in t: 
            counterT[char] = 1+counterT.get(char, 0)


        for char in s:
            if counterS[char]!=counterT.get(char, 0):
                return False

        return True