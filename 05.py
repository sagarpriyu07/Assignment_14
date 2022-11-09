#find smallest number in a given list
num=input("Enter numbers separated by comma(,)=")
l=[int(e) for e in num.split(',')]
print("Smallest numbr in a list",l,"is",min(l))