

def sum_list(nums):
    if len(nums) == 1:
        return nums[-1]
    
    return nums[0] + sum_list(nums[1:])
    




l = [t for t in range(200)]
print(sum_list(l))