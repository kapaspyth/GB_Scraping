import requests
from pprint import pprint
import json


username = str(input("Please enter the username: "))
url = "https://api.github.com/users/" + username + "/repos"
response = requests.get(url)
j_data = response.json()
repnames = []
for i in j_data:
    for j in i:
        if j == "name":
            rep = i.get(j)
            repnames.append(rep)
print(f'User {username} has the next depositories: {repnames}')

j_data_out = {
    "name": username,
    "name_of_depos": repnames,
}

with open('user_depos.json', 'w') as json_file:
  json.dump(j_data_out, json_file)
