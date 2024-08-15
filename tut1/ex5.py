
def checkTriangle(a, b, c):
    if a==0 or b==0 or c==0:
        return False
    else:
        if a+b > c and a+c>b and b+c>a:
            return True
        else:
            return False

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(checkTriangle(a, b, c))
