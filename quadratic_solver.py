import math

print("Welcome to Quadratic Solver!")
print("Please enter the coefficients a, b and c of the quadratic equation ax^2 + bx + c = 0:")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

# calculate the discriminant
d = b**2 - 4*a*c

# check if the roots are real
if d >= 0:
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print(f"\nThe roots are real and are: {x1} and {x2}")
else:
    print("\nThe roots are complex and cannot be computed.")
