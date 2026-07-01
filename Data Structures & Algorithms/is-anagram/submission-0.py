class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = dict()
        td = dict()
        for c in s:
            if c in sd.keys():
                sd[c]+=1
            else:
                sd[c]=0
        for c in t:
            if c in td.keys():
                td[c]+=1
            else:
                td[c] = 0
        if sd == td:
            return True
        return False
        