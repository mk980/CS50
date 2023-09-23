# x = float(input("what is x?: "))
# y = float(input("what is y?: "))

# z = round (x / y, 2)
# print (f"{z:.2f}")

# def main ():
#     x = (input("what's x? "))
#     print ("x square is", square (x))
    
# def square (n):
#     return n ** 2

# if __name__ == "__main__":
#     main()
    
    
#define a function for calculating square

def main ():
    x = int(input('what is the value of x? ')) # ask user to insert value of x
    print ('value of square is', square (x))
    
def square (n):
    return n**2
    # return pow(n, 2)

if __name__ == "__main__":
    main ()