#sort given list
num=input("Enter numbers separated by comma(,)=")
l=[int(e) for e in num.split(',')]
print("Sorted list of",l,"is",sorted(l))