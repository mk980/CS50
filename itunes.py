import json 
import requests
import sys

if len(sys.argv) != 2:
    sys.exit ()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=20&term=" + sys.argv [1])
# print (json.dumps(response.json(), indent=2))
tracks_name = response.json()
for track in tracks_name ["results"]:
    print (track["trackName"])
    