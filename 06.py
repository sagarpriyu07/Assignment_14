#find sum of elements in a given list
num=input("Enter numbers separated by comma(,)=")
l=[int(e) for e in num.split(',')]
print("Sum of elements in a list",l,"is",sum(l))