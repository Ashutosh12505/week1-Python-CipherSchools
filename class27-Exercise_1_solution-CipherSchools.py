# Ask the user to give three inputs and find the average of the three given numbers.
num1 = input("Enter the first number here:")
num2 = input("Enter the second number here:")
num3 = input("Enter the third number here:")

# (int(num1) + int(num2) + int(num3)) / 3
print(f"Average of the three given numbers is : {(int(num1) + int(num2) + int(num3)) / 3}")

#Another method.

a, b, c = input("Enter three numbers comma separated:").split(",")
print(f"Average of the three given numbers is : {(int(a) + int(b) + int(c)) / 3}")