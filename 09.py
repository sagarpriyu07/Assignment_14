#print indices of all occurance of the given element in the list
num=input("Enter numbers separated by comma(,)=")
list=[int(e) for e in num.split(',')]
x=int(input("indices of all occerances of which element you want to know="))
c=0
for i in range(len(list)):
    if list[i]==x:
        c+=1
        print(c,"occurance of",x,"at index",i)
