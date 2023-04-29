# Write a class structure that implements a library. Classes:
#
# 1) Library - name, books = [], authors = []
#
# 2) Book - name, year, author (author must be an instance of Author class)
#
# 3) Author - name, country, birthday, books = []
#
# Library class
#
# Methods:
#
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.
#
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
#
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
#
# All 3 classes must have a readable __repr__ and __str__ methods.
#
# Also, the book class should have a class variable which holds the amount of all existing books

def writeText(item):
    print(item)


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.books.append(book)
        if author not in self.authors:
            self.authors.append(author)
        author.books.append(book)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __str__(self):
        return writeText(f'books: {", ".join([book.name for book in self.books])}, author: {", ".join([author.name for author in self.authors])}, name: {self.name}, func: str')

    def __repr__(self):
        return writeText(f'books: {", ".join([book.name for book in self.books])}, author: {", ".join([author.name for author in self.authors])}, name: {self.name}, func: repr')


class Book:
    count = 0
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.count +=1

    def __str__(self):
        return writeText(f'author: {self.author}, name: {self.name}, func: str')

    def __repr__(self):
        return writeText(f'author: {self.author}, name: {self.name}, func: repr')



class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return writeText(f'name: {self.name}, country: {self.country}, books: {", ".join([book.name for book in self.books])},  func: str')

    def __repr__(self):
        return writeText(f'name: {self.name}, country: {self.country}, books: {", ".join([book.name for book in self.books])}, func: repr')


newlib = Library('first')
author1 = Author('Taras', 'Ukraine', 1678)
author2 = Author('Taras2', 'Ukraine', 1678)
newlib.new_book('Kobzar', 1700, author1)
newlib.new_book('Kobzar2', 1700, author1)
newlib.__str__()
newlib.__repr__()
author1.__str__()
author1.__repr__()
author2.__repr__()