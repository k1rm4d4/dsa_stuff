from typing import List 


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)): 
                if nums[i] == nums[j]:
                    print(f"{i}->{nums[i]}, {j}->{nums[j]}")
                    return True 
        return False




sol = Solution()
# resp = sol.containsDuplicate([1,2,3,4,5,6,2,4,4])
resp = sol.containsDuplicate([1])
print(resp)

# edge cases: 
# [1]