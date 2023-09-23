# name = input("Who is in the house? ")
# if name == "Harry" or name == "Ron" or name == "Hymoni":
#     print ("Gryfindor")

# elif name == "Draco":
#     print ("Slythrin")
    
# else:
#     print ("Who? ")

# match name:
#     case "Harry" | "Hermione" | "Ron":
#         print ("Gryffindor")
#     case "Draco":
#         print ("Slytherin")
#     case _:
#         print ("who?")
        
family = input ("tell about you family members: ")

match family:
    case "Fiaz" | "Riaz" | "ajaz":
        print ("brother")
    case "khizra" |"Sidra" | "Iqra":
        print ("sister")
    case "Charagh" | "Bilqees":
        print ("Parent")
    case "Sadi":
        print ("Spouse")
    case _:
        print ("Not Family")
        
