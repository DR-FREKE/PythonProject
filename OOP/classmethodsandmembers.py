class Book:
    # create attribute at class level so all instance method can use it
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # a good example for demonstrating a static method
    # create a private variable using the double underscore
    __booklist = None

    # create a static method that can list out all book list
    # we do this by using the static method decorator
    @staticmethod
    def getBookList():
        # remember to always use the class name to call the private variable
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    @classmethod
    def getBookType(cls):
        return cls.BOOK_TYPES

    def __init__(self, title, booktype):
        self.title = title
        if(not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a book type")
        else:
            self.booktype = booktype

    def setTitle(self, title_name):
        self.title_name = title_name


b1 = Book("shawcross", "EBOOK")
b2 = Book("Lame man walk", "HARDCOVER")

book_list = Book.getBookList()
book_list.append(b1)
book_list.append(b2)

print(book_list)
