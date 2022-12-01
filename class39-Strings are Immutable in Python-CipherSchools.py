# strings are immutable
a = "abcde"

print(a.replace("b","B")) # returns aBcde

a.replace("b","B")
print(a) # returns abcde
