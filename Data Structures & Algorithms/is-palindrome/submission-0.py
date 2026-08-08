class Solution:
    def isPalindrome(self, s: str) -> bool:
        first, last = 0, len(s)-1
        s = s.lower()
        while first <= last:
            if s[first].isalnum() == False :
                first += 1
            if s[last].isalnum()== False:
                last -= 1

            if s[first] == s[last]:
                first += 1
                last -= 1
            else:
                return False

        return True
