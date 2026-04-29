class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for anagram in strs:
            sort = tuple(sorted(anagram))
            if sort in output:
                output[tuple(sorted(anagram))].append(anagram)
            else:
                output[tuple(sorted(anagram))] = [anagram]
        return list(output.values())