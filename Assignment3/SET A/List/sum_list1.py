#SET-A.1)Write a python program to sum all the items in a list

list=[]
n=int(input("Enter the limit:"))
print("Enter the list elements:")
for i in range(n):
    ele=int(input())
    list.append(ele)
print("List Sum:",sum(list))