for i in range(1,11):
    if i==5:
        break
    else:
        print(i,end=" ")
print()
for i in range(1,11):
    if i==5:
        continue
    else:
        print(i,end=" ")
print()
for i in range(1,11):
    if i==5:
        pass #nullify effect
    print(i,end=" ")
