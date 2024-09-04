from stack import Stack

def rev_string(my_str):
    s = Stack()
    rev_str = ""
    for l in my_str:
        s.push(l)
    
    for _ in my_str:
        rev_str += s.pop()
    return rev_str

print(rev_string("apple"), "elppa")
print(rev_string("x"), "x")
print(rev_string("1234567890"), "0987654321")
