# Check for validity parantheses of types: 
# []{}(]){{}[][())]}


def check_balance_paranthesis(s: str)-> bool:
    stk = []
    for l in s: 
        if l in "([{":
            stk.append(l)
        else: 
            # exit()
            if len(stk) == 0: 
                # print("stk is zero")
                return False
            elif match( stk[-1], l): 
                # print("debug", stk[-1], l)
                stk.pop()
            else: 
                return False
    
    # print(stk)
    if stk == []:
        return True 
    else: 
        return False      
                
                
def match(last: str, current: str)-> bool:
    open_index = "([{".index(last)
    close_index = ")]}".index(current)
    # print(open_index, close_index)
    if open_index == close_index:
        return True 
    return False 


print(check_balance_paranthesis("(((())))"))
print(check_balance_paranthesis("(()((())()))"))
print(check_balance_paranthesis("()"))
print(check_balance_paranthesis("()[]{}"))
# # false cases
print(check_balance_paranthesis("([)]"))
print(check_balance_paranthesis("((((((())"))
print(check_balance_paranthesis("()))"))
print(check_balance_paranthesis("(()()(()"))
print(check_balance_paranthesis("]"))
print(check_balance_paranthesis("(])"))
