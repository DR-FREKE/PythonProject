class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # TODO : use the __str__ method to return a string representation
    def __str__(self):
        return f"Book Title : {self.title}\nBook Author : {self.author}"

    # TODO : use the __repr__ method to return an object representation
    def __repr__(self):
        return f"title={self.title}, author={self.author}, price={self.price}"


book1 = Book("Burning Light", "McFlair", 29.99)
book2 = Book("The catcher in the rye", "JD Salinger", 33.59)

# print(str(book2))
# print(repr(book2))
print(book1.__str__())
