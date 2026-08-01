a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

if a > b:
    if a > c:
        print("Largest number is: ", a)
    else:
        print("Largest number is: ", c)
else:
    if b > c:
        print("Largest number is: ", b)
    else:
        print("Largest number is: ", c)