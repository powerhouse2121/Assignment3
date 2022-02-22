#SET-A.1)Write a python program to multiplies all the items in a list

m=1
list=[]
n=int(input("Enter the limit:"))
print("Enter the list elements:")
for i in range(n):
    ele=int(input())
    list.append(ele)
    m=m*ele
print("List Product:",m)