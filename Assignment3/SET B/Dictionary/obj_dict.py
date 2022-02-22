#Write a python program to get a dictionary from an object's fields.

class dictobj(object):
    def __int__(self):
        self.x='red'
        self.y='yellow'
        self.z='Green'
    def do_nothing(self):
        pass
test=dictobj()
print(test.__dict__)
