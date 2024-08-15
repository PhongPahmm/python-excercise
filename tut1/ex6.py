def decimalToBinary(decimal, base):
    stack = []
    string = ""
    if decimal == 0:
        return 0
    while decimal > 0:
        remainder = decimal % base
        stack.append(remainder)
        decimal //= base

    while len(stack) != 0:
        string+= str((stack.pop()))

    return str(string)

print(decimalToBinary(5, 2))