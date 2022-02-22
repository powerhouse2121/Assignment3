#Write a python program to check whether an element is exists within a tuple

tup=(1,2,3,4,5)
ele=int(input("Enter the element to search:"))
flag=0
for i in range(len(tup)):
    if(tup[i]==ele):
        flag=1
if(flag==1):
    print("Element Exists")
else:
    print("Element not Exists")