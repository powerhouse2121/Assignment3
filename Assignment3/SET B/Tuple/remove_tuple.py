#Write a python program to remove an item from a tuple

tup=(1,2,3,4,5)
print(tup)
lst=list(tup)
del lst[2]
tup=tuple(lst)
print(tup)