students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Raveclaw"}
]

# houses = []
# for student in students:
#     if student["house"]  not in houses:
#         houses.append(student["house"])

# for house in sorted(houses):
#     print (house)

houses = set()
for student in students:
    houses.add(student["house"])
    
for house in sorted(houses):
    print (house)