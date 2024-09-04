# run from parent dir contatining file stack.py 
# py3 -m examples.simple_bln_parantheses

from stack import Stack 

# paran = input()

def check_balanced(parantheses):
    s = Stack()
    for brkt in parantheses:
        if s.is_empty():
            s.push(brkt)
            # print(brkt, s)
            continue
        last = s.peek()
        if last == brkt:
            s.push(brkt)
        else: 
            s.pop()
        # print(brkt, s)

    # print(parantheses, s)
    if s.is_empty():
        return True
    else:
        return False
    
# true cases
# print(check_balanced("(())"))
print(check_balanced("(()()()())"))
print(check_balanced("(((())))"))
print(check_balanced("(()((())()))"))
# false cases
print(check_balanced("((((((())"))
print(check_balanced("()))"))
print(check_balanced("(()()(()"))

