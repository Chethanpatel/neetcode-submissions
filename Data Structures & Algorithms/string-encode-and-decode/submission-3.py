class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        
        decoded = []
        pointer = 0

        while pointer < len(s):
            if s[pointer].isdigit() and s[pointer+1] == '#':
                length = int(s[pointer])
                decoded.append(s[pointer+2:pointer+2+length])
                pointer+=length+2
        
        return decoded


