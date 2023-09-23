# # Ask user for their name
# name = input ("what is your name? ").strip().title()

# # #remove white space from the string and capitalize user's name
# # name = name.strip().title()

# # # Capitalize user's name
# # name = name.title()

# first, last = name.split (" ")

# # say hello to user
# print (f"hello, {last}")


import sys

#check for errors
# if len (sys.argv) < 2:
#     sys.exit ("Too few arguments")
# elif len (sys.argv) > 2:
#     sys.exit ("too many arguments")

for arg in sys.argv[1:]:
    
#print name tags    
    print ("Hello, may name is", arg)