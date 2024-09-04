

def infix_to_postfix(infix):
    # parse the string and get the list for processing
    infix_list = infix.split()
    # init op_stack 
    op_stack = []
    # init output list
    output = []
    # init a list to check for operators 
    operators = "*/-+"
    op_preced = ["/", "*", "+", "-"]
    # list to check for alphabet A to Z
    operands = "ABCDEFGHIJKLMNOPQRSTWUVXYZ"
    # list to check for paranthesis or maybe dict 
    paran = {
        "(": ")"
    }
    # A * B + C * D --> AB * CD * + 
    print("INPUT: ", infix_list)
    for token in infix_list:
        print("Token: ", token)
        print("OP_STACK: ", op_stack)
        print("OUTPUT: ", output)
        # alphabet/operands
        if token in operands: 
            output.append(token)
        # left paranthesis check
        elif token in paran.keys():
            op_stack.append(token)
        # right paranthesis check 
        elif token in paran.values(): 
            popped = op_stack.pop()
            while popped != "(":
                if popped in operators:
                    output.append(popped)
                popped = op_stack.pop()
        # operators
        elif token in operators: 
            if op_stack != []:
                last_op = op_stack[-1]
                if last_op in operators: 
                    while op_preced.index(last_op) <= op_preced.index(token): 
                        print(last_op, token, op_preced.index(last_op) , op_preced.index(token))
                        p = op_stack.pop()
                        print(p)
                        output.append(p)
                        if op_stack:
                            last_op = op_stack[-1]
                        else: 
                            break
            op_stack.append(token)


                # while op_preced.index(op_stack[-1]) <=  op_preced.index(token):
                #     print(op_stack[-1], token, op_preced.index(op_stack[-1]), op_preced.index(token))
                #     p = op_stack.pop()
                #     output.append(p)
                #     if op_stack != []:
                #         break
    
    while op_stack != []:
        output.append(op_stack.pop())

    return " ".join(output)

# print(infix_to_postfix("A + B * C + D")) # 
# print(infix_to_postfix("A * B + C * D"))
# print(infix_to_postfix("A + B + C + D"))
print(infix_to_postfix("( A + B ) * ( C + D )"))