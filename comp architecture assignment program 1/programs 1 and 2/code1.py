def to_8bit(n):
    """Convert an integer to 8-bit 2's complement."""
    return format(n & 0xFF, '08b')


def signed_value(binary):
    """Convert 8-bit 2's complement to signed decimal."""
    value = int(binary, 2)
    if value >= 128:
        value -= 256
    return value


def binary_arithmetic(a, b, operation):
    print("\nOperand A:", a, "=", to_8bit(a))
    print("Operand B:", b, "=", to_8bit(b))

    if operation == '+':
        result = a + b
        print("\nBinary addition:")
        print(" ", to_8bit(a))
        print("+", to_8bit(b))
        print("----------")
    else:
        result = a - b
        print("\nBinary subtraction:")
        print(" ", to_8bit(a))
        print("-", to_8bit(b))
        print("----------")

    binary_result = to_8bit(result)
    overflow = result < -128 or result > 127

    print("Binary result :", binary_result)
    print("Decimal result:", result)
    print("Overflow      :", "Yes" if overflow else "No")


print("a) (+46) + (+29)")
binary_arithmetic(46, 29, '+')

print("\nb) (-48) - (-23)")
binary_arithmetic(-48, -23, '-')