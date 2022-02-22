#Write a python script to generate and print a dictionary that contains
#a nuber(between 1 and n)in the form(x,x*x)

n=int(input("Enter the number:"))
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)