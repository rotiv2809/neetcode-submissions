class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = {}
        sort = {}
        count = 0
        for i, n in enumerate(strs):
            key = "".join(sorted(n))
            if key in sort:
                hs[n] = sort[key]  
            else:
                sort[key] = count
                hs[n] = count
                count += 1

        answer = [[] for _ in range(count)]
        for n in strs:
            answer[hs[n]].append(n)
        return answer

            
            