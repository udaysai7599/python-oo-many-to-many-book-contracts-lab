#!/usr/bin/env python3

class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        # return all contracts related to this book
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # return all authors related to this book
        return [contract.author for contract in Contract.all if contract.book == self]


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        # return all contracts related to this author
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        # return all books related to this author
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalties):
        # create and return a new contract
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # sum royalties across all contracts for this author
        return sum(contract.royalties for contract in Contract.all if contract.author == self)


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # validations
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        # return all contracts with matching date
        return [contract for contract in cls.all if contract.date == date]
