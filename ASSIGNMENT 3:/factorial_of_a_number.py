def factorial():
    n = int(input("Enter the number: "))
    _factorial = 1
    counter = n
    while counter > 0:
        _factorial *= counter
        counter -= 1
    print("The factorial of",n,"is",_factorial)
factorial()