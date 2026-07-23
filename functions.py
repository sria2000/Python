#. Predefined function - like len etc
#. Userdefined function - customize
#. Anonymous function - nameless function like pandas

# Basic Function. Print will just print the message
def welcome_message():
    print("Hello Mate ..")

welcome_message()

# Use return to update the original value
def addition(first_number,second_number,third_number):
    return print(first_number+second_number+third_number)

addition(10,100,1000)

# Details passed via position argument
def get_details(name,place,expected_price):
    print("Client Name:",name)
    print("Place of Birth:",place)
    print("expected_price",expected_price)


get_details("Sri","Chennai", 9.7)

get_details(expected_price=11.99, place="Bangalore",name="Ram")
print(" ")
# Default Parameters & Arguments
def get_details_chennai(name,expected_price,place="Chennai"):
    print("Client Name:",name)
    print("Place of Birth:",place)
    print("expected_price",expected_price)
get_details_chennai("Sriram",32)

print(" ")
## Have multiple values. Variable length arguments
print ("Shows or prints multiple values")
    
def get_details_delhi(name,place,*expected_price):
    print("Client Name:",name)
    print("Place of Birth:",place)
    print("expected_price",expected_price)

get_details_delhi("Boss","Delhi",90,91.1,98,100)


print(" ")
## Keyword Argument
print ("Shows or prints multiple values represending Keyword Arguments")
    
def get_details_delhi(name,place,**expected_price):
    print("Client Name:",name)
    print("Place of Birth:",place)
    print("expected_price",expected_price)

get_details_delhi("Boss","Delhi",ask_1 = 90,ask_2 = 91.1,ask_3 =98,ask_4 = 100)