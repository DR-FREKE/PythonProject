from dataclasses import dataclass

# Dataclasses provides us the ability to use default values


@dataclass
class Book:
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = 0.0


b1 = Book()

print(b1)


# one rule about using default values in dataclasses is that any instance variable without a
# a default value must come first and must be passed as an arguement when the class is instatiated
@dataclass
class Book2:
    price: float
    title: str = "No Title"
    author: str = "No Auhtor"
    pages: int = 0


b2 = Book2(0.0)
print(b2)
