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
            start = pointer

            if s[pointer] != '#':
                pointer += 1

            length = int(s[start:pointer])

            pointer += 1

            decoded.append(s[pointer:pointer+length])
            pointer += length

        return decoded

