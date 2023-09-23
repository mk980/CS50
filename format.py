# import re

# name = input ("what's your name? ").strip()
# # if "," in name:
# #     last, first = name.split(", ")
# #     name = (f"{first} {last}")
# # print (f"hello, {name}")
# matches = re.search(r"^(.+), (.+)$", name) #using () to group
# if matches:
#     # last, first = matches.groups () # we can remove variable also as follow
#     # name = f"{first} {last}"
#     name = matches.group (2) + " " + matches.group(1)
# print (f"hello, {name}")

import re

name = input("what is you your name? ").strip()
if matches := re.search (r"^(.+), *(.+)$", name):

    name = matches.group(2) + " " + matches.group(1)

print (f"hello, {name}")