Movie_names = ["Harry potter","spider man","super man","Master","Super delux","Arjun Reddy","Dil bechara","Banglore days"]
# New_Movie = []
# for i in Movie_names:
#     if 'a' in i:
#         New_Movie.append(i)
New_Movie = [i for i in Movie_names if 'a' in i] 
print(New_Movie)