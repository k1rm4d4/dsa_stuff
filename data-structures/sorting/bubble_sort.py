


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


t = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(bubble_sort(t))
print(bubble_sort([2]))
print(bubble_sort([2, 0]))
print(bubble_sort([5, -7, 2, 0]))


