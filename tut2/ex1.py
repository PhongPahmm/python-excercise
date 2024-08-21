def CountLetters(str):
    upper = lower = other = 0
    for char in str:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        else:
            other += 1
    return upper, lower, other

str = input("Enter a string: ")
upper, lower, other = CountLetters(str)
print(f"Uppercase letters: {upper}, Lowercase letters: {lower}, Other characters: {other}")