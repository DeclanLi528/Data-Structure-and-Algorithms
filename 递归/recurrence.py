from pythonds3.basic import Stack
import turtle

def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])
    
# 递归三原则
# 1. 递归算法必须有基本情况
# 2. 递归算法必须改变其状态并向基本情况靠近
# 3. 递归算法必须递归地调用自己

# 将整数转换成2-16为进制基数的字符串
def to_str(n,base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n//base, base)\
        + convert_string[n % base]
    
def to_str(n, base):
    r_stack=Stack
    convert_string = "0123456789ABCDEF"
    while n > 0:
        if n<base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[n%base])
        n = n//base
    res = ""
    while not r_stack.is_empty():
        res=res + str(r_stack.pop())
    return res

# ------------------------------------------------------------------------------
my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def draw_spiral(my_turtle, line_len):
    if line_len > 0 :
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)

draw_spiral(my_turtle, 100)
my_win.exitonclick