import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = re.sub(r'[^a-zA-Z0-9]', '', s.casefold())
        p2 = len(clean_str) - 1
        p1 = 0
        while p1 < p2:
            if clean_str[p1] != clean_str[p2]:
                return False  
            p1 += 1
            p2 -= 1 
        return True 
    
sol = Solution()
s = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s))