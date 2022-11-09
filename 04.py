#find greatest number in a given list
num=input("Enter numbers separated by comma(,)=")
l=[int(e) for e in num.split(',')]
print("Greatest numbr in a list",l,"is",max(l))