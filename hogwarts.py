# students = ["Hermione", "Harry", "Ron", "Draco"]
# # houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

# students = {"Hermione": "Gryffindor", 
#             "Harry": "Gryffindor", 
#             "Ron": "Gryffindor", 
#             "Drace": "Slytherin"
# }

# # for i in range (len(students)):
# #     print (i+1, students[i])


# print (students ["Hermione"])

# for student in students:
#     print (student, students[student], sep= ", ")


# students = [
#     {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None}
# ]


# a = next (item for item in students if item ["patronus"] == "Stag")
# print (a)
# # for student in students:
#     print (student ["name"], student ["house"], student ["patronus"], sep = ", ")

# x=[i["patronus"] for i in students if i.get("patronus")=='Stag']
# print(x[0] if x else None)


nested_dict = {'bulldog': {'type': 3}, 'cat': {'type': 4}, 'yorkie': {'type': 11}, 'pitbull': {'type': 8}}
new = {k: v for k, v in nested_dict.items () if v['type'] % 2 != 0}
print (new)