# using multiple inheritance in python

class A:

    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Solomon"


class B:

    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Ndifereke"


# this is how you inherit multiple classes
class C(A, B):
    def __init__(self):
        super().__init__()

    def showProps(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


c1 = C()
c1.showProps()

# use this to show the method resolution order of class i.e the hiarachy of all classes
print(C.__mro__)
