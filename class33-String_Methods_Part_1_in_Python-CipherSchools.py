# string methods (we use . in methods)
# we can either directly print the outpur or store them in a new variable.

# (1)  length method -- to get the length of any string.
   #Also counts the spaces given in between the words in the string.

q = "Ashutosh Kumar Singh"
print(len("Ashutosh Kumar Singh"))
#or
print(len(q))

# (2) lower() method -- returns all characters after converting them in lower alphabets (small letters).
print(q.lower())

# (3) upper() method -- returns all characters after converting them in upper alphabets (capital letters).
print(q.upper())

'''
  (4) title() method -- returns all characters after converting the
 first word of each letter in upper alphabets (capital letters) and,
 after converting all other letters in lower alphabets (small letters).
'''
print("royal challangers bangalore".title())  # returns "Royal Challangers Bangalore".

# (5) count() method -- counts number of characters in a string.
#  (case sesitive, i.e. A & a are diff for this method)

q = "Ashutosh Kumar Singh"

#syntax = variable/string.count("value")
# print(q.count())  -- wrong, at least one argument needed.
print(q.count("a"))
print(q.count("A"))
print(q.count("z"))
print(q.count("h"))