#Isaac Arthur
#10/18
def add(x, y):
    print("After a second check")
    return x + y

def subtract(x, y):
    print("After a second check")
    return x - y

def multiply(x, y):
    print("After a second check")
    return x * y

def divide(x, y):
    print("After a second check")
####    if !0:
####        print("You can't divide by zero.")
##        return x / y

def remainder(x, y):
    print("After a second check")
    return x % y

print("Select Operation:")
print("+ Add")
print("- Subtract")
print("* Multiply")
print("/ Divide")
print("% Remainder")

choice = input("Enter choice(+,-,*,/,%):")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '+':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '-':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '*':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '/':
   print(num1,"/",num2,"=", divide(num1,num2))
elif choice == '%':
   print(num1,"%",num2,"=", remainder(num1,num2))

else:
   print("Invalid input")
