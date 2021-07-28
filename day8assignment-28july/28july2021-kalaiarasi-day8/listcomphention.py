movienames=["action","master","spiderman","titanic","alien","joker","karnan","maara"]
#newmovie=[]
#for i in movienames:
 #  if "a" in i:
 #      newmovie.append(i)
#print(newmovie)
new=[i for i in movienames if 'a' in i]
print(new)


#num=[2,4,5,3,8,7]
#new=[i for i in num if i%2==0]
#print(new)

lan=["english","tamil","civic","river","rotor","madam","malayalam","example","running","noon"]
pal=[i for i in lan if i==i[::-1]]
print(pal)

#dynamic list
#li=[i for i in range(2,501) if i%2!=0]
#print(li)

#lan=["english","tamil","civic","river","rotor","madam","malayalam","example","running","noon"]
#new=[i.replace("noon","morning") for i in lan]
#print(new)



