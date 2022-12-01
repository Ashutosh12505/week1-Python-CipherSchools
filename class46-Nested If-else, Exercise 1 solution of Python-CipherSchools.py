num = 65
num_in = int(input("Enter the number here."))
if num == num_in:
    print("You win !!!")
else:
    if num>num_in:
        print("Too low")
    else:
        print("Tow high")