from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float


b1 = Book("saw mill", "mike dean", 34, 40.99)

# great thing about dataclasses is it make available the magic methods automatically

print(b1.price)
