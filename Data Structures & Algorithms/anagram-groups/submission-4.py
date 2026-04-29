class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res = defaultdict(list)
        # sort each string as hash in default dict {'abc': ['acb', 'bca']} O(nlogk)
        # set each string as hash in default dict {'abc': ['acb', 'bca']} O(n) but does not hash the same
        for word in strs:
            #work around set as hashkey
            # - make a bitmask of each key
            # if set(word) == set(key)
            res[str(sorted(word))].append(word)
        return list(res.values())