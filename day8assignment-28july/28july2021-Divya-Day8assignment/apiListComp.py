import json
import  requests
data = requests.get ("https://jsonplaceholder.typicode.com/posts")
Extractdata = data.json()
titleList = [ ]
for i in Extractdata:
    titleList.append(i['title'])
    #print(titleList)
new = [ x for x in titleList if x[0]=='a' in x]
print(new)