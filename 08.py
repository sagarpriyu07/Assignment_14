#print distinct elements along with their frequencies of occurance in the list
l=[12,43,12,54,67,32,54,21,43,75]
s=list(set(l))
print("List is",l,s)
for i in range(len(l)):
    for j in range(len(s)):
        if l[i]==s[j]:
            print("Element",s[j],"-",l.count(l[i]),"times")
            s.remove(s[j])
            break
        
