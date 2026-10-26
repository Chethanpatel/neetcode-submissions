class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
    
        # Sort the array lexicographically
        strs.sort()
        
        # Take the first and last strings
        first = strs[0]
        last = strs[-1]
        
        prefix = []
        
        # Compare characters of the first and last string
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            prefix.append(first[i])
            
        return "".join(prefix)

        