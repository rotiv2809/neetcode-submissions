class Solution:
    def isValid(self, s: str) -> bool:
        v = [0,0,0]
        lead = []
        for c in s:
            if c == '(':
                v[0]+=1
                lead.append('x')
            if c == ')':
                if lead == []: return False
                if (lead[-1] != 'x'):
                    return False
                v[0]-=1
                lead.pop()
            if c == '[':
                v[1]+=1
                lead.append('y')
            if c == ']':
                if lead == []: return False
                if (lead[-1] != 'y'):
                    return False
                v[1]-=1
                lead.pop()
            if c == '{':
                v[2]+=1
                lead.append('z')
            if c == '}':
                if lead == []: return False
                if (lead[-1] != 'z'):
                    return False
                v[2]-=1
                lead.pop()
        print(v)
        if v == [0,0,0]:
            return True
        else:
            return False
                
            
            