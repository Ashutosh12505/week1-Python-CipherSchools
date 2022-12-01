num = input("Enter your number here :")

sum = 0

r = 0

while r < len(num):
    sum = sum + int(num[r])
    r += 1
print(sum)