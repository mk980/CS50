# first, _ = input("what's your name? ").split()
# print (f"hello, {first}")


# def total(galleons: int, sickles: int, knuts: int) -> int:
#     return (galleons * 17 + sickles) * 29 + knuts

# # # coins = [100, 50, 25]

# # # print(total (*coins), "knuts")

# coins = {"galleons": 100, "sickles": 50, "knuts": 25}

# print (total(**coins), "knuts") # ** unpacks dictionaries while * unpack lists
# # print (galleons=100, sickles=50, knuts=25, "knuts")


def f(*args, **kwargs):
    print ("Named:",kwargs)
    print ("Positional:", args)
    
f(100, 50, 10, 3)
    
f(galleons=100, sickles=50, knuts=25)



