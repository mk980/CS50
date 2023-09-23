# import re 

# email = input ("what's you email? ").strip() # strip() removes spaces before and after

# # username, domain = email.split("@")

# # if username and domain.endwith(".edu"):
# #     print("Valid")
# # else: 
# #     print ("Invalid")

# if re.search(r"^(\w|\.)+@(\W+\.)?\w+\.edu$", email, re.IGNORECASE): 

# ''' 
# re.search (pattern, string, flag=0) re.match (patter, string, flag=0), re.fullmatch (pattern, string, flag=0) on both sides
# caret (^) sign indicate start with, while $ means ends with, 
# adds optional subdomain, r stands for raw string (read more about raw string)''' 
    
#     print("Valid")
# else:
#     print ("Invalid ")
import re

email = input("what's your email ?" ).strip() 

if re.search (r"^[/w]+@[/w]+\.edu$", email, re.IGNORECASE):
    print ("valid")
else:
    print ("invalid")