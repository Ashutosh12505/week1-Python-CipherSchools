# Centre method.
ab = "Royal"
#syntax = variable.centre(total length of characters and items to be added,what to be added)
print(ab.center(9,"#")) # two at both sides each
print(ab.center(6,"#")) # only one at right side

#Practice
n1 = input("Please enter your name here:")
print(n1.center(len(n1)+8,"*"))