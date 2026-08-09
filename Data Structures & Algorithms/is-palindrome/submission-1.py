class Solution:
    def isPalindrome(self, s: str) -> bool:
        first, last = 0, len(s)-1
        s = s.lower()
        while first < last:
            if self.alphaNum(s[first]) == False :
                first += 1
            if self.alphaNum(s[last]) == False:
                last -= 1

            if s[first] == s[last]:
                first += 1
                last -= 1
            else:
                return False

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
