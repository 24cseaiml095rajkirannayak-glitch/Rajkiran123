# WAP to create 4 basic classes having individual methods addition(), substraction(), multiplication(), division() respectively. Create a derived class for all above (multiple inheritance) having member data: data1, data2. Create a derived class for all above multiple object and the operations on the detail & data1 & data2.

class Add:
    def add(self, a, b):
        print("addition :", a+b)

class sub:
    def sub(self, a, b):
        print("subtractor :", a-b)

class mul:
    def mul(self, a, b):
        print("multiplication :", a*b)

class Div:
    def div(self, a, b):
        print("division :", a/b)

class calculator(Add, sub, mul, Div):
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

a = float(input("Enter first number:"))
b = float(input("Enter second number:"))

obj = calculator(10, 5)
obj.add(obj.data1, obj.data2) 
obj.sub(obj.data1, obj.data2)
