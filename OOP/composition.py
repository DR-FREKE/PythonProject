# creating a composition

# using the default inheritance
class Book:
    def __init__(self, title, price, authorfname, authorlname, ):
        self.title = title
        self.price = price
        self.authorfname = authorfname
        self.authorlname = authorlname

        self.chapter = []

    # append more chapters to the chapter array
    def addChapter(self, name, pages):
        self.chapter.append((name, pages))


# b1 = Book("How to get away with murder", 54.99, "Solomon", "Ndifereke")
# b1.addChapter("Chapter 1", 125)
# b1.addChapter("Chapter 2", 129)
# b1.addChapter("Chapter 3", 290)

# print(b1.title)


# using COMPOSITION
class Book:
    def __init__(self, title, price, author=None):  # default author to be none
        self.title = title
        self.price = price
        self.author = author

        self.chapters = []

    # function to add chapters into the empty array by appending
    def addChapter(self, chapter):
        self.chapters.append(chapter)

    # function to count to pages in chapter array
    def getPageCount(self):
        result = 0
        for ch in self.chapters:
            result += ch.pagecount
        return result


# a class to hold all authors
class Author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    # its python way of overriding the toString() method and return the result as a string
    # in Java we, override the toString() method
    def __str__(self):
        return f"{self.fname} {self.lname}"


# class to hold the chapters
class Chapter:
    def __init__(self, name, pagecount):
        self.name = name
        self.pagecount = pagecount


b1 = Book("How to get away with murder", 45.99, Author("Solomon", "Ndifereke"))
b1.addChapter(Chapter("chapter 1", 23))
b1.addChapter(Chapter("chapter 2", 40))

print(b1.title)
print(b1.author)
print(b1.getPageCount())
