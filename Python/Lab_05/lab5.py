import math

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

print(first_number, "^", second_number, "=", math.pow(float(first_number), float(second_number)))

print("The square root of", first_number, "=", math.sqrt(float(first_number)))

print("The square root of", second_number, "=", math.sqrt(float(second_number)))

print("The ceiling of", first_number, "/", second_number, "=", math.ceil(float(first_number) / float(second_number)))

print("The floor of", first_number, "/", second_number, "=", math.floor(float(first_number) / float(second_number)))

print("Absoulute difference between", first_number, "and", second_number, "=", abs(float(first_number) - float(second_number)))

print("Area of a circle with radius", first_number, "=", math.pi * (float(first_number) ** 2))

print("Hypotenuse of a right triangle with sides", first_number, "and", second_number, "=", math.hypot(float(first_number), float(second_number)))