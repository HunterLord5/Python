class Parent:

    def __init__(self):
        print("This is parent class")

    def parentfunc(self):
        print("This is parent method")

    def func(self):
        print("calling from parent class")


p = Parent()


class Child(Parent):
    def __init__(self):
        print("This is child class")

    def childfunc(self):
        print("This is child function")

    def func(self):
        print("Calling from child func")


c = Child()
c.childfunc()
c.func()
