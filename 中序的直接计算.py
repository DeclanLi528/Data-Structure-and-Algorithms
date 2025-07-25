#结合中序转后序的转换法 和 后序表达式的算法，直接实现中序计算
# 在计算时，应该使用两个stack处理中序的表达式标记

#假设中序表达法为 ( ( 1 + 2 ) * ( 3 + 4 ) )
#遇到op先存，存时如果存的优先级低于存入的，弹出直接计算
#中序是从左往右，而非从右往左
#入站的时候用push LIFO last in first out
from pythonds3.basic import Stack

def precedence(op):
    if op in ("*" , "/"):
        return 2 
    if op in ("+" , "-"):
        return 1
    return 0


def mid_eval(midfix_expr):
    op_stack = Stack()
    num_stack = Stack()
    token_list = midfix_expr.split()

    for token in token_list:
        if token.isnumeric():
            num_stack.push(int(token))
        elif token == "(" :
            op_stack.push(token)
        elif token == ")":
            while not op_stack.is_empty() and op_stack.peek() != "(":
                op = op_stack.pop()
                right = num_stack.pop()
                left = num_stack.pop()
                try:
                    result = do_math(op, left, right)
                except ZeroDivisionError:
                    print("Zero is not allowed as divisor")
                    return None
                num_stack.push(result)
            op_stack.pop()#把“（”弹掉

        else:
            while (not op_stack.is_empty() and precedence(op_stack.peek())
                   >= precedence(token)):
                op = op_stack.pop()
                right = num_stack.pop()
                left = num_stack.pop()
                try:
                    result = do_math(op, left, right)
                except ZeroDivisionError:
                    print("Zero is not allowed as divisor")
                    return None
                num_stack.push(result)
            op_stack.push(token)#把比栈内小的检测到的运算符放进栈内

    #清理剩下的运算符
    while not op_stack.is_empty():
        op = op_stack.pop()
        right = num_stack.pop()
        left = num_stack.pop()
        result = do_math(op, left, right)
        num_stack.push(result)

    return num_stack.pop()


def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    if op == "/":
        if op2 == 0:
            raise ZeroDivisionError
        else:
            return op1 / op2
    if op == "+":
        return op1 + op2
    if op == "-":
        return op1 - op2

print(( ( 1 + 2 ) * ( 3 + 4 ) ))