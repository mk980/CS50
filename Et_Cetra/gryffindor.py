# students = [
#     {"Name": "Hermione", "house": "Gryffindor"},
#     {"Name": "Harry", "house": "Gryffindor"},
#     {"Name": "Ron", "house": "Gryffindor"}, 
# #     {"Name": "Draco", "house": "Slytherin"} 
# ]

# gryffindors = [
#     student["Name"] for student in students if student["house"] == "Gryffindor"
    
# ]


# for gryffindor in sorted(gryffindors):
#     print (gryffindor)


# def is_gryffindor (s):
#     return s["house"] == "Gryffindor"

# gryffindors = filter(is_gryffindor, students)


# for gryffindor in sorted(gryffindors, key=lambda s:s["Name"]):
#     print(gryffindor["Name"])


#dictionary comprehension

# students = ["Hermione", "Harry", "Ron"]

# # gryffindors = [{"name":student, "house": "Gryffindor"} for student in students]

# gryffindor = {student : "Gryffindor" for student in students}



    
# print (gryffindor)



#enumerate

# students = ["Hermione", "Harry", "Ron"]

# for i, student in enumerate(students):
#     print (i+1, student)
    


