# This is Task1 which explains about String Functions in Python

First_Name =  " Sriram "
Last_Name = " V a r a d h a r a j a n   "

# Convery to Upper
print(" ")
print(" Convert to Upper")
print(First_Name.upper())
print(Last_Name.upper())

#Convert to Lower
print(" ")
print(" Convert to Lower")
print(First_Name.lower())
print(Last_Name.lower())

#Strip space
print(" ")
print(" Strip space")
print(First_Name.strip())
print(Last_Name.strip())

# Replace all spaces
print( " ")
print(" Replace all spaces in last name")
print(Last_Name.replace(" ",""))

# Replace String
print(" ")
print("Replace String")
print(First_Name.replace("Sriram", "Sri"))
print(Last_Name.replace('V a', 'vA'))


#Capitalize
print(" ")
print("Capitalize")
print(First_Name.capitalize())
print(Last_Name.capitalize())

# Convert to List
print(" ")
print("Convert to List")
print(First_Name.split())
print(Last_Name.split())

#Count occurances of letter a in Last Name
print(" ")
print(" ount occurances of letter a in Last Name")
print(Last_Name.count("a"))

# Swap case
print(" ")
print(" Swap the case ")
print(First_Name.swapcase())
print(Last_Name.swapcase())

#SLICING
print(" ")
print("First name Slicing")
print(First_Name[1])
print(First_Name[-2])

#Mix Match
age = 40
fullname = First_Name.replace(" ","") + " " + Last_Name.replace(" ","")
print(f"My Full Name is {fullname} and I am {age} years old")