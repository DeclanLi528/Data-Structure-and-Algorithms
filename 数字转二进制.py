def decimal_to_binary(n):
    remainders = []

    while n > 0:
        remainder = n % 2
        remainders.append(remainder)
        n = n // 2

    remainders.reverse() 

    binary = ''.join(str(bit) for bit in remainders)

    return binary , remainders

number = 17
binary_result, remainders = decimal_to_binary(number)

print(f"十进制 {number} 的二进制表示是:{binary_result}")
print(f"转换过程中的余数是:{remainders}")



# 将十进制数转换成任意进制数
from pythonds3.basic import Stack

def base_converter(decimal_num, base):
    digits = '0123456789ABCDEF'
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num % base
        rem_stack.push(rem)
        decimal_num = decimal_num // base

    
    new_string = ''
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string