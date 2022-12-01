name = input("Enter your name :")
box = ""
i = 0
while i < len(name):
    if name[i] not in box:
        box += name[i]
        print(f"{name[i]} : {name.count(name[i])}")

    i += 1