name, character = input("Enter your name and desired character comma separated:").split(",")
print("The length of your name is:",str(len(name)))
#or
print(f"The length of your name is : {len(name.strip())}") #strip used to remove the begininng and ending extra spaces.

print("The character count is:",str(name.count(character))) # This will be case sensitive
# to make it case in-sensitive, we both the inputs in either lower type or upeer type.
a=name.upper()
b=character.upper()
print("The character count is:",str(a.count(b)))  # typecasting used.Coverts name and character in upper letters

#solving the issue of counting of spaces given during input of name and character in the terminal (by using strip method and replace method for the in-between spaces).

a3 = name.replace(" ","")
print(f"The length of your name is : {len(a3)}")
print(f"The character count in the name is : {name.lower().count(character.strip().lower())}") #Coverts name and character in lower letters.