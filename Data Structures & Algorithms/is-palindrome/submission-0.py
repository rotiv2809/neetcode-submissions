class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cleaning the spaces
        word = []
        word_inv = []
        for i in s:
            if i == ' ':
                pass
            elif ((i <= 'Z' and i >= 'A') or (i <= 'z' and i >= 'a') or (i <= '9' and i >= '0')):
                word.append(i)

        # inverting
        for i in range(len(word)-1,-1,-1):
            word_inv.append(word[i])

        print(word)
        print(word_inv)
        
        for i, c in enumerate(word):
            if word_inv[i].lower() == c.lower():
                pass
            else:
                return False

        
        return True