movies=["Sultan","Singam","Master","HarryPotter","Karnan","Spiderman","24","3","96"]
new_movies=[i for i in movies if "a" in i]
# for i in movies:
#     if 'a' in i:
#         new_movies.append(i)
# print(new_movies)
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even=[i for i in numbers if i%2==0]
# print(even)

newlist=["english","tamil","civic","river","rotor","madam","malayalam","example","running","noon"]
odd=["morning" if i=="noon" else i for i in newlist]
print(odd)