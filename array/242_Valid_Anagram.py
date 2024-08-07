class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        lcount_s = {}
        lcount_t = {}
        for sl, tl in zip(s ,t): 
            if lcount_s.get(letter) is not None:
                lcount_s[letter] += 1
            else: 
                lcount_s[letter] = 1

        for letter in t: 
            if lcount_t.get(letter) is not None:
                lcount_t[letter] += 1
            else: 
                lcount_t[letter] = 1

        # print(lcount_s)
        # print(lcount_t)
        if lcount_s == lcount_t:
            return True
        
        return False


s = Solution()
print(s.isAnagram("cat", "car"))
print(s.isAnagram("anagram", "nagaram"))