name = input("Enter your name here :")
age = int(input("Enter your age :"))

if age > 10:
    if name[0] == "a" or name[0] == "A":
        print('You are allowed')
    else:
        print("Sorry, your name isn't in the category")

else:
    print("Sorry, you are under-age")