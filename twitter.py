import re
''' sub function of re module

re.sub(pattern, sub, string, count, flag)'''


url = input ("URL: ").strip()

# Username = re.sub(^"(https?://)?(www.\)?twitter\.com/", "", url)
# print (f"Username:{Username}")

if matches:= re.search(r"^https?://(?:www\.)twitter\.com/([a-z0-9_])$", url, re.IGNORECASE):
    print (f"Username:", matches.group(1))