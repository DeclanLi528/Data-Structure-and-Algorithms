from pythonds3.basic import Stack


def infix_to_postfix(expr):
    precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    output = []
    op_stack = Stack()
    tokens = expr.split()
    for token in tokens:
        if token.isalnum():
            output.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top = op_stack.pop()
            while top != "(":
                output.append(top)
                top = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (
                precedence[op_stack.peek()] >= precedence[token]
            ):
                output.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        output.append(op_stack.pop())
    return " ".join(output)


result = infix_to_postfix("( A + B ) * ( C + D )")
print(result)


# 用python 实现后序表达式的计算
def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()

    for token in token_list:
        if token.isnumeric():
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)

            operand_stack.push(result)
    return operand_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    if op == "/":
        return op1 / op2
    if op == "+":
        return op1 + op2
    if op == "-":
        return op1 - op2


print(postfix_eval("1 2 + 3 4 + *"))
