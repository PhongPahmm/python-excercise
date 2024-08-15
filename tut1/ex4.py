def binaryToDecimal(binary):
    base = 1
    decimal = 0

    while binary > 0:
        remainder = binary % 10
        decimal += remainder * base
        base *= 2
        binary //= 10

    return decimal

binaryValue = int(input("Enter a binary number: "))
print(binaryToDecimal(binaryValue))
