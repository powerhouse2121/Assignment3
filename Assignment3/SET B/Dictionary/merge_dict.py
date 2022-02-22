#Write a python script to merge two python dictionaries

d1={'a':100,'b':200}
d2={'c':300,'d':400}
d=d1.copy()
d.update(d2)
print("MERGED DICTIONARY:",d)
