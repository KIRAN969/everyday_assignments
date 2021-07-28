Li_Num = [1,4,53,6,78,5,85,44,88,99,100]
new = [i for i in Li_Num if i%2==0 ]
print(new,end =" ")
name = ["english","tamil","civic","river","rotor","madam","malayalam","example","running","noon"]
new =[i for i in name if i==i[::-1]]
print(new)

numbers = [i for i in range(3,11)]
print(numbers,end=" ")

num = [i for i in range(2,500) if i %2==1]
print(num)
new_name = [i.upper() for i in name ]
print(new_name,end=" ")
new = [i.replace("noon","morning") for i in name]
print(new)