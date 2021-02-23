from dataclasses import dataclass, field
import random

# Dataclasses provides us another way to use default value by importing the field function from
# the dataclass calss


def default_price():
    return float(random.randrange(20, 40))


@dataclass
class Book:
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    # we can create a default value that is calculated from a function
    price: float = field(default_factory=default_price)


b1 = Book()

print(b1)
