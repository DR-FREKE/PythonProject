from dataclasses import dataclass, field

# Dataclasses provides us another way to use default value by importing the field function from
# the dataclass calss


@dataclass
class Book:
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default=10.0)


b1 = Book()

print(b1)
