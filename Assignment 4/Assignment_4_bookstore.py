# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 13:01:02 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""


class Book:

    """A class that defines a Book object.

    An instance has the book's title and weight.

    Attributes:
        title (string): the published title of the book
        weight (float): the shipping weight of the book in pounds

    """

    def __init__(self, title, weight):
        """Called: Book(title, weight)"""
        self.title = title
        self.weight = weight

    def __str__(self):
        return str(self.title)


class ForSaleBook(Book):

    """A class that defines a Book object that is for sale.

    An instance has a book's title, weight, and sale price.

    Subclass of:
        Book: adds attribute 'price' (the book's sale price), extends
            __init__() to include "price"

    Attributes:
        title (string), from Book: the published title of the book
        weight (float), from Book: the shipping weight of the book in pounds
        price (float): the sale price of the book

    """

    def __init__(self, title, weight, price):
        """Called: ForSaleBook(title, weight, price)"""
        Book.__init__(self, title, weight)
        self.price = price

    def __str__(self):
        return f'{self.title} (${self.price:.2f})'


class ExaminationCopy(Book):

    """A class tjat defines a Book object that is an examination copy.

    An instance has a book's title, weight, and the person's name who is
    examining it.

    Subclass of:
        Book: adds attribute 'receiver' (the book's examiner), extends
            __init__() to include "receiver"

    Attributes:
        title (string), from Book: the published title of the book
        weight (float), from Book: the shipping weight of the book in pounds
        receiver (string): the name of the person examining the book

    """

    def __init__(self, title, weight, receiver):
        """Called: ExaminationCopy(title, weight, receiver)"""
        Book.__init__(self, title, weight)
        self.receiver = receiver

    def __str__(self):
        return f'{self.title} ({self.receiver})'


class Box:

    """A class that defines a Box object that contains Book objects.

    An instance has the box's ID, capacity, and contents list.

    Attributes:
        ID (int): the identification number of the box
        capacity (float): the total weight of book objects allowed within the
            content list
        content (list): a list of Book objects held within the box

    Methods:
        add_book(bk): appends a Book object, bk, to the content list
        total_weight(): returns the sum of the weight of all Book objects in
            the content list of the box
        print_content(): prints the __str__ of each Book object in the content
            list of the box

    """

    def __init__(self, ID, capacity, content=[]):
        """Called: Box(ID, capacity, content)"""
        self.ID = ID
        self.capacity = capacity
        self.content = content

    def __str__(self):
        return str(self.ID)

    def add_book(self, bk):
        """Tries to add a Book object to the box's content list.  If the book
        would exceed the box's capacity it will print a ValueError exception
        message"""
        if (self.total_weight() + bk.weight) > self.capacity:
            raise ValueError('Capacity of ' + str(self) + ' exceeded')
        self.content.append(bk)

    def total_weight(self):
        """Returns the sum of the weight of each Book in the content list"""
        total = 0
        for b in self.content:
            total += b.weight
        return total

    def print_content(self):
        """Prints the __str__ of each Book in the content list"""
        for b in self.content:
            print(b.__str__())


if __name__ == '__main__':
    fs_bk = ForSaleBook('MobyDick', 3.5, 12.50)
    print(str(fs_bk) + ' has weight ' + str(fs_bk.weight) + ' pounds.')
    ex_cp = ExaminationCopy('Little Women', 2.7, 'Fred')
    print(str(ex_cp) + ' has weight ' + str(ex_cp.weight) + ' pounds.')
    print('-' * 40)
    bx = Box(12, 10.0)
    bx.add_book(fs_bk)
    bx.add_book(ex_cp)
    bx.add_book(ForSaleBook('Catch 22', 3.2, 10.75))
    bx.print_content()
    try:
        bx.add_book(ExaminationCopy('Networks: An Introduction', 3.7, 'Al'))
    except ValueError as detail:
        print(detail)
