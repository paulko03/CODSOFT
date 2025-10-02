#3) Calculator

print("CALCULATOR")
print("Select the operation you wanna execute")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Division")
choice = input("Enter choice(1 -> 4):")
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
if choice == '1':
    print("Result:", num1 + num2)
elif choice == '2':
    print("Result:", num1 - num2)
elif choice == '3':
    print("Result:", num1 * num2)
elif choice == '4':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
            print("Error: Division by zero is not allowed.")
else:
    print("Invalid input")
