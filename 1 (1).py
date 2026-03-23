a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

# Arithmetic operations
s = a + b
d = a - b
p = a * b
if b != 0:
    div = a / b
else:
    div = None

print("Sum:", s)
print("Difference:", d)
print("Product:", p)
print("Division:", div)

# Even / odd
print(a, "is", "even" if a % 2 == 0 else "odd")
print(b, "is", "even" if b % 2 == 0 else "odd")

# Convert one to float
a_float = float(a)
print("a as float:", a_float)
