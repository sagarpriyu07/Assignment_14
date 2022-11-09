#remove all non int values from the list
l=[32,"hello",31.2,23.4,"world",53,12,64,"mysirg","python",34,"c"]
while len(l):
    for i in range(len(l)):
        if type(l[i])!=int:
            l.remove(l[i])
            break
    else:
        break
print(l)