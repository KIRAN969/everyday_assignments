import json
import requests
data=requests.get("https://jsonplaceholder.typicode.com/posts")
extractedata=data.json()
tit=[]
for i in extractedata:
    tit.append(i['title'])
lis=[i for i in tit if i[0]=='a' or i[0]=='A']
print(lis)