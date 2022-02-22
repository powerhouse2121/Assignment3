#Write a python program to check if a set is a subset of another set

s1=set({1,2,3,4,5,6,7})
s2=set({1,2,3,5,6})
s3=s2.issubset(s1)
print(s3)