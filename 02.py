#create a list of first n odd natural number
num=int(input("Enter any number="))
l=[]
for i in range(1,2*num,2):
    l.append(i)
print(l)