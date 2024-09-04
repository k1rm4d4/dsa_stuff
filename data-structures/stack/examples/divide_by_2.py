import math 

from stack_list import Stack 

def get_binary(num):
    """
    Get Binary representation of any integer
    
    """
    bin_str = ""
    if num < 0:
        
    else:
        s = Stack()
        num_str = str(num)
        print(num_str)
        dividend = num 
        while dividend != 0: 
            rem = dividend % 2
            dividend = dividend // 2
            print((rem, dividend))
            s.push(rem)
        # print(s)


        while not s.is_empty(): 
            bin_str += str(s.pop())

    return bin_str


print(get_binary(56)) # 111000
print(get_binary(42)) # 111000
print(get_binary(-31)) # 111000
