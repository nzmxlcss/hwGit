s1 = "Hello"
s2 = "Hello"
s3 = "2"
s4 = "Hello ´World´"
s5 = '''one 
two 
three'''
#print(s1, s2, s3, s4, s5)


#Конкатенація
print ("Concetenate: ",s1 +" World!")

# String formatting
#age = 18
#age2 =14
#a= f"Age is {age}"
#b = "Age is {}".format(age2)
#print (a + "\n"+b)

# \n
print("Hello\nWorld! 1 2 3")

# \t
print("Hello World!\nHello\tWorld!")

#\\
print("Name \"Alex \"")

# str methods
s = "Hello World!"
print(s.replace("World", "Python"))


print("Count o", s.count("o"))
print("12345 length ", len("12345"))

s = "The quick brown fox"
print(s.split(" "))
s_split = s.split("-")

print("\t".join(s_split))


# Slices
symbol = s [0]
print(symbol)
print("Last symbol ", s[-2])
print(s[0:5])