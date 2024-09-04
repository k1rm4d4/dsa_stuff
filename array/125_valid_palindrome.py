class Solution:
    def isPalindrome(self, s: str) -> bool:
        sp = 0 
        ep = len(s) -1 
        while sp < ep:
            # print(s[sp], sp, s[ep], ep)
            while not s[sp].isalnum():
                sp += 1
                # print("not", s[sp], s[ep])
            while not s[ep].isalnum():
                ep -= 1
                # print("not", s[sp], s[ep])
            if s[sp].lower() != s[ep].lower():
                return False
            sp += 1
            ep -= 1
            
        return True 
           

    
    

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("s"))