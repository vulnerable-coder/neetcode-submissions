import string
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        t = defaultdict(list)
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            k = tuple(count)
            t[k].append(word)
        return list(t.values())