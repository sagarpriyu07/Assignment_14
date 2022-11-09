#create a list of first n even natural number
num=int(input("Enter any number="))
l=[]
for i in range(2,2*num+1,2):
    l.append(i)
print(l)