from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i in nums: 
            if map.get(i) is not None: 
                # map[i] += 1
                return True 
            else: 
                map[i] = 1
        return False



s = Solution()
print(s.containsDuplicate([1,2,3,4])) # false
print(s.containsDuplicate([1,2,3,1])) # true 
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # true 