name = "  Ashutosh  "
title = "Singh"
print(name + title) #prints with all spaces present to the left and to the right of the name.
print(name.lstrip() + title) #removes all the space present to the left of the name.
print(name.rstrip() + title) #removes all the space present to the right of the name.
print(name.strip() + title) #removes all the spaces present to the left and to the right of the name.

n2 = "Ashu   tosh"
print(n2.replace(" ","")) #replaces all the space (" ") by empty place("").