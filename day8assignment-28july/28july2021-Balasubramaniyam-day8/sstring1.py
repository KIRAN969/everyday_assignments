import requests,json

from requests.models import stream_decode_response_unicode
data=requests.get("https://jsonplaceholder.typicode.com/posts")
string=data.json()
print(isinstance(string,list))
titlelist=[]
for i in string:
    titlelist.append(i['title'])
#print(titlelist)
alist=[i for i in titlelist if i[0]=='a' or i[0]=='A']
print(alist)