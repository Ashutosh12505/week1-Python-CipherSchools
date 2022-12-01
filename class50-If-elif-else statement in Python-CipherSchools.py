age = input("Enter your age :")
age = int(age)

if age == 0:
    print("You aren't allowed")
elif 0<age<=3 :
    print("Free ticket")
elif 3<age<=10 :
    print("Ticket price : 150")
elif 10<age<=60 :
    print("Ticket price : 250")
elif age > 60:
    print("Ticket price : 200")

else:
    print("Enter correct value of age.")