class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    # TODO: the __eq__ method should check for equality between two objects
    def __eq__(self, value):
        # check if what given is an object
        if not isinstance(value, Book):
            raise ValueError("can't compare book to a non-book")
        return (self.title == value.title and self.author == value.author and self.price == value.price)

    # TODO: the __ge__ method should establish a greater (>=) relationship with another object
    def __ge__(self, value):
        if not isinstance(value, Book):
            raise ValueError('cannot compare book to a non-book')
        return (self.title > value.title)

    # TODO: the __lt__ method should establish a lesser than (<) relationship with another object
    def __lt__(self, value):
        if not isinstance(value, Book):
            raise ValueError('cannot compare book to a non-book')
        return (self.price < value.price)


book1 = Book("War and Peace", "Leo Tolstoy", 39.95)
book2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
book3 = Book("War and Peace", "Leo Tolstoy", 39.95)
book4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# TODO : Check for equality
# print(book1 == book3)  # print now uses the __eq__()
# print(book1.__eq__(book3))  # we prefer to use this

# print(book1.__eq__(book2))

# try:
#     print(book1.__eq__(42))
# except ValueError:
#     print('error')

# TODO: Check for greater than and less than value
# print(book2.__ge__(book1))

# TODO: sort the list
# since the built in function uses the less than operator we can automatically sort the list

books = [book1, book2, book3, book4]
books.sort()
# comprehension method of looping an array and still maintaining it in an array 
print([book.title for book in books])
