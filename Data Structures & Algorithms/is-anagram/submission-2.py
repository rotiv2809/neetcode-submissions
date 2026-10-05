class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter([])
        ss = len(s)
        st = len(t)
        if(ss != st):
            return False
        
        for i in range(st):
            c[t[i]]+=1

        for i in range(ss):
            if (s[i] not in c):
                return False
            c[s[i]]-=1
        
        print(c)

        if all(v == 0 for v in c.values()):
            return True

        else:
            return False