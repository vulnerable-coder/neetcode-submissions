import string

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        t = {}
        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            k = tuple(count)
            if k in t:
                t[k].append(word)
            else:
                t[k] = [word]
        return list(t.values())