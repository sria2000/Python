# Accept Multiple User inputs
# Basic script to accept your firstname, lastname and age and print the values

First_name = input("Enter Users first name ")
Last_name = input("Enter Users last name ")
# abs will force to positive if negative is written
age = abs(int(input("Enter  your age: ")))
address = input("Enter your address with postcode ")

full_details = input(f"Your full name is {First_name}  {Last_name} and you are {age} years old. You live in {address} \n")
