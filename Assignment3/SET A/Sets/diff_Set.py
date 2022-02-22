#Write a python program to create set difference.

x=set({'ANMOL','SHRIRAMPUR','AHEMEDNAGAR'})
x1=set({'P','ANMOL','AURANGABAD'})
x2=x.difference(x1)
print(x2)
x2=x1.difference(x)
print(x2)