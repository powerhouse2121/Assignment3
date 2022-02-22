#SET-B.1)Write a python program to remove duplicate from a list

l=[]
n=int(input("Enter the limit:"))
for i in range(n):
    ele=int(input())
    l.append(ele)
print("Original list:",l)
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print("Unique elements:",l1)