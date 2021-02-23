from dataclasses import dataclass, field

# we can make the attribute of the class immutable i.e not changeable by setting frozen in the
# decorator to be TRUE


# a decorator can accept arguement
@dataclass(frozen=True)
class Book:
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default=10.0)

    # if we created a function to modify the attribute, it will throw an error
    def somefunc(self, newvalue):
        self.title = newvalue


b1 = Book()

# b1.title = "Wassa"
# print(b1.title)

b1.somefunc("new value")
