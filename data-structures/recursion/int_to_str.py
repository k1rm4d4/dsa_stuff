# problem: convert any int (base-10) to its string representation.
# example: 32746 --> "32746"


def convert(num: int)-> str:
    digit_str_map = {i: f"{i}" for i in range(10)}
    if num < 10:
        return digit_str_map[num]
    
    ld = num % 10
    num = num // 10
    print(ld," ", num)
    return convert(num) + convert(ld)

ans = convert(32746)
print(ans, type(ans))