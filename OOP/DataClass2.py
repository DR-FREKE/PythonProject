from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # dataclasses allows us create additional instance variable that may rely on already created
    # instance variable and this runs after the init function in the dataclass has finished running
    def __post_init__(self):
        self.description = f"{self.title} by {self.author} and price of {self.price}"


b1 = Book("saw mill", "mike dean", 34, 40.99)

print(b1.description)
