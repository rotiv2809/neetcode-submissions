class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1 or len(s) == 0:
            return len(s)
        charSet = set({})
        values = []
        index1 = 0
        index2 = 0
        m = 0
        for _ in range(len(s)):
            if (s[index2] in charSet):
                values.append(index2 - index1)
                while(s[index2] in charSet):
                    charSet.remove(s[index1])
                    index1+=1
            charSet.add(s[index2])
            index2+=1
        if values != []:    
            return max(max(values),index2-index1)
        else:
            return index2-index1
