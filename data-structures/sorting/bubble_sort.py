def swap(nums, idx_a, idx_b):
    # print("init:: ", nums[idx_a], nums[idx_b])
    temp = nums[idx_b]
    nums[idx_b] = nums[idx_a]
    nums[idx_a] = temp
    # print("final:: ", nums[idx_a], nums[idx_b])


def bubble_sort(nums):
    if len(nums) == 1:
        return nums
    index = 0
    curr = nums[index]
    curr_nxt = nums[index + 1]
    while index + 1 < len(nums):
        curr = nums[index]
        curr_nxt = nums[index + 1]
        # print("idx, curr, curr_next: ", index, curr, curr_nxt)
        if curr > curr_nxt:
            swap(nums, index, index + 1)
            index += 1
        else:
            index += 1

    return nums


def bubble_sort2(nums):
    for _ in range(len(nums)):
        for i in range(len(nums) - 1):
            p_val = nums[i]
            nxt_val = nums[i + 1]
            if p_val > nxt_val:
                p_val, nxt_val = nxt_val, p_val
                nums[i] = p_val
                nums[i + 1] = nxt_val
    return nums


t = [54, 26, 93, 17, 77, 31, 44, 55, 20]


print(t, " <-input")
# print(bubble_sort2(t) == [17, 20, 26, 31, 44, 54, 55, 77, 93])
assert bubble_sort2([54, 26, 93, 17, 77, 31, 44, 55, 20]) == [
    17,
    20,
    26,
    31,
    44,
    54,
    55,
    77,
    93,
]
assert bubble_sort2([4, 1, 3, 4, 2, 2]) == [1, 2, 2, 3, 4, 4]
assert bubble_sort2([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert bubble_sort2([42]) == [42]
assert bubble_sort2([]) == []

