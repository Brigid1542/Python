def divide(x, y):
    return x / y

try:
    print(divide(40, 0))
except ZeroDivisionError as e:
    print(e, "Division by zero not possible",)
    print(e.__class__)
except Exception as e:
    print("Something went wrong!")
