# def main ():
#     print_square (3)
    
# def print_square (size):
#     for i in range (size):
#         print_row (size)
        
# def print_row (width):
#     print ("#" * width)

# main ()

def main ():
    print_square (3)
        
def print_square (size):
    for i in range (size): # for each row in square
        
        for j in range (size): # for each brick in row
            print ("#", end= "") #print brick
            
        print () #print a new line
main ()


