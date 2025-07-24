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

