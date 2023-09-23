# def main ():
#     x = get_int ("What's x? ")
#     print (f"x is {x}")

# def get_int (prompt):
#     while True:
#         try:
#             return int(input(prompt))
#             # print (f"x is {x}")
#         except ValueError:
#             # print ("x is not an integer")
#             pass
#         # else:
#         #     return x


# main ()



def main ():
    x = get_number("what's x? ")
    print (f"x is {x}")
    
    
def get_number (prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:

            pass
        
    
main ()