import math
def calculate_operations():
    number = float(input("Enter a number: "))

    square_root = math.sqrt(number)
    natural_log = math.log(number)
    sine_value = math.sin(number)
    print("For the number:",number)
    print("Square root:",square_root)
    print("Natural logarithm:",natural_log)
    print("Sine (in radians):",sine_value)

calculate_operations()