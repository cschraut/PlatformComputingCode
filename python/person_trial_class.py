class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return self.fname, self.lname
    
    def sayHello(self):
        print("hello, my name is", self.fname, self.lname)
    