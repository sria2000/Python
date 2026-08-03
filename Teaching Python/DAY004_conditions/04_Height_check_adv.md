
# Enter Height of the person
# if height is over 120cm he can ride else he isinit
# Check age. if age is 18 & over £15 else if age between 12 and less than 18 pay £10 else pay £5

height = float(input("What's your height"))
if height >= 120:
   print("Yaay!! You can ride the game")
   age = int(input("What is your age"))
   if age >=18:
       print("You need to pay £15 to ride the game")
   elif age >=12 and age <18:
       print("You need to pay £10 to ride the game")
   else:
       print("You need to pay £5 to ride the game")
else:
   calc = int(120 - height)
   print(f" Oops. You are short by {calc}cms . come next year")
