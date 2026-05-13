class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = {}
        for item in s:
            if not c.get(item):
                c[item] = 1
            else:
                c[item] += 1
        
        for item in t:
            if not c.get(item) or not c.get(item,0)>0:
                return False
            else:
                c[item] -=1
        for _, v in c.items():
            if v!=0:
                return False
        return True