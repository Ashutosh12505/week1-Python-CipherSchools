#Replace method

sen1 = "Water water everywhere, and all the boards did shrink.Water water everywhere, nor any drop to drink."
print(sen1.replace("water","air")) # case sensitive, only replaces words with same case(doesn't replace "Water").
a=sen1.replace("every","_") # works
print(a)

b = "For men may come and men may go but I go on forever."
print(b.replace(" ","_"))
print(sen1.replace(" ","_",5))  # will replace first 5 " " by "_"
print(sen1.replace(" ","_"))
print(sen1.replace(" ","*"))
print(b.replace(" ","_____"))

#Find method

p = "It is an ancient Mariner,And he stoppeth one of three.'By thy long grey beard and glittering eye,Now wherefore stopp'st thou me?"

#beginning of the string which has been put in the argument is considered to give the position.

t=p.find("ancient") #9
u=p.find("anci")    #9
v=p.find("ient")    #12
#all these (t,u,v) give the same result.

w=p.find("it") # The first word isn't printed, case sensitive.
x=p.find("B")

print(t)
print(u)
print(v)
print(w)
print(x)
print(p.find("stoppeth"))

abc = "Peter piper picked a peck of pickled peppers."
pqr = " Peter piper picked a peck of pickled peppers."

print(abc.find("Peter")) # 0
print(pqr.find("Peter")) # 1 because space is present at first position.

print(abc.find("pi",20)) # will start searching only after 20.

# to find position of second "pi" withput knowing the position of the first one.

z = abc.find("pi")
print(abc.find("pi",z + 1))