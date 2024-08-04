

class Solution:
    def twoSum0(self, nums, target: int) :
        map = {}
        for i, x in enumerate(nums):
            c = target - x
            # print("c->", c)
            # print(map)
            if x in map.keys(): 
                a = map[x]
                return [a[0], i]
            else: 
                map[c] = [i, x]
                # print(map)


    def twoSum(self, nums, target: int):
        map = {}
        for i, x in enumerate(nums):
            c = target - x
            if map.get(c) is not None:
                return [map.get(c), i]
            else: 
                map[x] = i



s = Solution()
print("RESULT", s.twoSum([3,2,4], 6))
print("RESULT", s.twoSum([0,4,3,0], 0))
print("RESULT", s.twoSum([2,7,11,15], 9))
print("RESULT", s.twoSum([3,3], 6))
print("RESULT", s.twoSum([2,10,-21,15], 9))

# print("RESULT", s.twoSum0([3,2,4], 6))
# print("RESULT", s.twoSum0([0,4,3,0], 0))
# print("RESULT", s.twoSum0([2,7,11,15], 9))
# print("RESULT", s.twoSum0([3,3], 6))