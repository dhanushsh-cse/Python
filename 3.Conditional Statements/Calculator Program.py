print("1.Add 2.Sub 3.Div 4.Multiply 5.Modulus")

num1 = int(input("Enter num1 value: "))
num2 = int(input("Enter num2 value: "))
ch = int(input("Enter the choice(1-5): "))
if ch == 1:
    print("Addition: ",num1 + num2)
elif ch == 2:
    print("Subtraction: ",num1 - num2)
elif ch == 3:
    print("Division: ",num1 / num2)
elif ch == 4:
    print("Multiplication: ",num1 * num2)
elif ch == 5:
    print("Modulus: ", num1 % num2)
else:
    print("Invalid Choice")         