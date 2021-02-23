class Publication:
    # abstract the ones' with most repeat i.e title and price
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publication):
    def __init__(self, title, publisher, price, period):
        Publication.__init__(self, title, price)
        self.publisher = publisher
        self.period = period


class Books(Publication):
    def __init__(self, title, author, price, page):
        # pass the title and price to the parent constructor using super.
        # we could also do this by calling the parent class instead of the super() keyword
        # Publication.__init__(self, title, price) also allowed; if you are using this method,
        # remember to pass the self in the parent class init function
        super().__init__(title, price)
        self.author = author
        self.page = page


class Magazines(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)


class NewsPaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, publisher, price, period)


# we can see duplicates in our classes; the better way to do it will be by using inheritance
# so we can define a parent class that has all this attribute and every child class will inherit this attributes

# we also see that NewsPaper class and Magazine class have exactly the same attribute
# so we can also scale that up for them to inherit from a parent class

m1 = Magazines("How to get away with murder", "Solomon", 45.99, 1225)
print(m1.title)
