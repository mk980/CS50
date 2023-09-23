# i = 5

# # while i != 0:
    
# #     print ('meow')
    
# #     i = i -1


""" write a function a say a cat 'meow' to a specific number of times"""
    
def main ():
    number = get_number ()
    meow (number)
def get_number ():
    while True:
        n = int (input ("what's n ? "))
        if n > 0:
            break
        
    return n

def meow (number):
    for _ in range (number):
        print ("meow")
main ()


