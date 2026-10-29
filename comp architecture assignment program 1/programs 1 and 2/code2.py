def rotate_right(value, positions):
    print("Rotate Right Without Carry (ROR)")
    print("Original:", value)

    for i in range(positions):
        value = value[-1] + value[:-1]
        print("Step", i + 1, ":", value)

    print("Final result:", value)


def rotate_right_carry(value, carry, positions):
    print("\nRotate Right With Carry (RCR)")
    print("Original:", value)
    print("Initial carry:", carry)

    for i in range(positions):
        new_carry = value[-1]
        value = str(carry) + value[:-1]
        carry = new_carry

        print("Step", i + 1, ":", value,
              "| Carry:", carry)

    print("Final result:", value)
    print("Final carry:", carry)


binary = "11010101"

rotate_right(binary, 3)

# Assume initial carry = 0
rotate_right_carry(binary, 0, 3)