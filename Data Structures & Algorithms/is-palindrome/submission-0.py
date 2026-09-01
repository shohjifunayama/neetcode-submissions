class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()

        n = len(s)
        
        for i in range(n):
            if s[i] != s[n-1-i]:
                return False
            
        return True
                


        