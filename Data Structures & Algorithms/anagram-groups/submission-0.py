class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for string in strs:
            alphabet_array = [0]*26

            for char in string:
                alphabet_array[ord(char) - ord('a')] += 1

            result[tuple(alphabet_array)].append(string)

        return list(result.values())
