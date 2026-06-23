try:
    a = int(input("Enter First Value: "))
    b = int(input("Enter Second Value: "))
    print("I am try just started")
    if b % 2 == 0:
        raise Exception("Even number")
    print(a / b)
    print("I am try, I am done")
except ZeroDivisionError as zd:
    print(zd)
except Exception:
    print("Division by evens are not allowed")
else:
    print("try is executed")
finally:
    print("Hello I am finally")