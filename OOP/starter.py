class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        # when we add double underscore to an attribute, python changes the name so other classes won't
        # be able to access this attribute and if they try apllication will throw an error
        # this can also be a way of declaring a variable private since python doesn't have the keyword private
        self.__secret = "this is a secret"

    def _getprice(self):
        # let the hasattr run through my code to check if the discount attribute exist
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setDiscount(self, amount):
        # a private attribute AKA private variable
        self._discount = amount


# b1 = Book("Brave new world")
b2 = Book("War in Peace", "Solomon", 12, 99.0)

print(b2._getprice())
b2.setDiscount(0.25)
print(b2._getprice())
print(b2._Book__secret)
