# Generators use yield keyword 

def main ():
    

    n = int(input("what's n? "))
    for s in sheep (n):
        print (s)


def sheep (n):
    
    for i in range (n):
        yield "n" * i
        
    
            
if __name__ =="__main__":
    main()