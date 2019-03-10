class random:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("self called")
    def getname(self):
        print("Your name is: " +self.name)
    def getage(self):
        print("Your age is: "+self.age)
p1 = random("Tanweer", "24")
p1.getname()
p1.getage()
