import random 
# Given array of nums: 
nums = [12,-44,67,6,-4,-11,56,7,89,-12,31,0] 

def binary_search(n, low, high, arr): 
    mid_ix = (low+high)//2
    mid_n = arr[mid_ix]
    # print(mid_ix)
    # print(n, mid_n)
    if n > mid_n: 
        low = mid_ix
        return binary_search(n, low, high, arr)
    elif n < mid_n: 
        high = mid_ix
        return binary_search(n, low, high, arr)
    elif n == mid_n: 
        return mid_ix
    else: 
        return None


# TEST 
# nums.sort()
# print(len(nums) - 1)

# manual
# ix = binary_search(0, 0, len(nums) - 1, nums)
# print(ix)

# automated tests: 
for i in range(10):
    # rnums = [random.randrange(-100, +100, i+1) for _ in range(20)]
    rnums = random.sample(range(-100,100, i+1), 20)
    rnums.sort()
    rindex = random.randrange(0, 19,1)
    t = rnums[rindex]
    # correct ix for this run must be i+1
    print(f"Correct index: {rindex} for {t}")
    print(rnums)
    print("RX::", binary_search(t, 0, len(rnums), rnums))