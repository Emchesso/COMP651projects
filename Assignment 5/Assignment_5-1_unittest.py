# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 15:09:33 2022

Ethan Chesson
COMP 651-001
Dr. Esterline
"""

import unittest
from bookstore import Book
from bookstore import ForSaleBook
from bookstore import ExaminationCopy
from bookstore import Box

class TestForSaleBook(unittest.TestCase):

    """A class that defines a TestCase for the ForSaleBook class.

    Methods:
        test_init_ForSaleBook(): tests the initialization of the object
        test_str_ForSaleBook(): tests the toString method
    """

    def test_init_ForSaleBook(self):
        """tests the initialization of the object"""
        print('test_init_ForSaleBook')
        testFSBook = ForSaleBook('testTitle', 5.0, 1.11)
        self.assertEqual(testFSBook.title, 'testTitle')
        self.assertEqual(testFSBook.weight, 5.0)
        self.assertEqual(testFSBook.price, 1.11)

    def test_str_ForSaleBook(self):
        """tests the toString method"""
        print('test_str_ForSaleBook')
        testFSBook = ForSaleBook('testTitle', 5.0, 1.11)
        self.assertEqual(str(testFSBook), 'testTitle ($1.11)')

class TestExaminationCopy(unittest.TestCase):

    """A class that defines a TestCase for the ExaminationCopy class.

    Methods:
        test_init_ExaminationCopy(): tests the initialization of the object
        test_str_ExaminationCopy(): tests the toString method
    """

    def test_init_ExaminationCopy(self):
        """tests the initialization of the object"""
        print('test_init_ExaminationCopy')
        testECBook = ExaminationCopy('testTitle', 4.0, 'testReceiver')
        self.assertEqual(testECBook.title, 'testTitle')
        self.assertEqual(testECBook.weight, 4.0)
        self.assertEqual(testECBook.receiver, 'testReceiver')

    def test_str_ExaminationCopy(self):
        """tests the toString method"""
        print('test_str_ExaminationCopy')
        testECBook = ExaminationCopy('testTitle', 4.0, 'testReceiver')
        self.assertEqual(str(testECBook), 'testTitle (testReceiver)')

class TestBox(unittest.TestCase):

    """A class that defines a TestCase for the Box class.

    Methods:
        setUp(): creates a testBox object for future tests
        tearDown(): sets the value of testBox to None
        test_total_weight(): tests that the weight attribute is correct
        test_add_book(): set to fail when adding a book that is exceeds testBox
            capacity
    """

    def setUp(self):
        """creates a testBox object for future tests"""
        print('setUp')
        self.testBox = Box(111, 10, [])
        bk1 = Book('', 5.0)
        bk2 = Book('', 4.0)
        self.testBox.add_book(bk1)
        self.testBox.add_book(bk2)

    def tearDown(self):
        """sets the value of testBox to None"""
        print('tearDown\n')
        self.testBox = None

    def test_total_weight(self):
        """tests that the weight attribute is correct"""
        print('test_total_weight')
        self.assertEqual(self.testBox.total_weight(), 9.0)

    @unittest.expectedFailure
    def test_add_book(self):
        """set to fail when adding a book that is exceeds testBox capacity"""
        print('test_add_book')
        bk3 = Book('', 2.0)
        self.testBox.add_book(bk3)

if __name__ == '__main__':
    unittest.main()
