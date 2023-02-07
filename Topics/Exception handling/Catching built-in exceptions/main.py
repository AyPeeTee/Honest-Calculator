a = int(input())
b = int(input())

try:
    a / b
except ZeroDivisionError:
    print("The Error!")
else:
    print(a / b)
