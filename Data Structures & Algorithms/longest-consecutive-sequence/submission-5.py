class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l = []
        ans = []
        max = 0
        def find_min(n: int) -> int:
            while (n-1) in s:
                n-=1
            return n
        
        def find_max(n: int) -> int:
            while (n+1) in s:
                s.remove(n)
                l.append(n)
                n+=1
            s.remove(n)
            l.append(n)
            return n
        
        while s:
            print(f'comecou em {next(iter(s))}')
            minimum = find_min(next(iter(s)))
            print(f'o minimo e {minimum}')
            find_max(minimum)
            ans.append(l)
            l=[]
        
        print(ans)

        for line in ans:
            if (len(line) > max):
                max = len(line)
        return max