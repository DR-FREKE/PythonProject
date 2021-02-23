class Book:
    def __init__(self, title):
        self.title = title


class NewsPaper:
    def __init__(self, name):
        self.name = name


# create some instance of the classes
b1 = Book("The catcher in the Rye")
b2 = Book("The grapes of wrath")

n1 = NewsPaper("the sunrise newspaper")
n2 = NewsPaper("the punch newspaper")

# we can use the type() function to check if two given objects are of the same type
print(type(b1) == type(b2))  # this will result to true
print(type(b2) == type(n2))  # this will result to false

# we can use the isinstance() function to check if a given object is an instance of a particular class
# isinstance() function takes two arguements; the object, and the class.

print(isinstance(b1, Book))  # this will result to true
print(isinstance(n1, NewsPaper))  # result to true
print(isinstance(n2, Book))  # result to false
print(isinstance(n2, object))  # result to true
