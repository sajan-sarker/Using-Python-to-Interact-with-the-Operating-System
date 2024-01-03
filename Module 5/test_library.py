import unittest
class Library:
    def __init__(self):
        self.collection = []
    def add_book(self, book_title):
        self.collection.append(book_title)
    def has_book(self, book_title):
        return book_title in self.collection
    
class TestLibrary(unittest.TestCase):
    def test_adding_book_to_library(self):
        library = Library()
        new_book = "Python Design Pattern."

        library.add_book(new_book)

        self.assertTrue(library.has_book(new_book))

library_test_output = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestLibrary))
print(library_test_output)