import json
import requests
data=requests.get("https://reqres.in/api/users?page=2")
extractedata=data.json()
#print(extractedata)
data=extractedata["data"]
for i in data:
    values=i["first_name"]
    print(str(values))