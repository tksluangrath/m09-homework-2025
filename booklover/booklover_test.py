import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        # add a book and test if it is in `book_list`.
        booklover = BookLover("Terrance", "vwy4sa@virginia.edu", "History")
        booklover.add_book("The Giver", 2)
        
        self.assertTrue("The Giver" in booklover.book_list["book_name"].values)

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        booklover = BookLover("Terrance", "vwy4sa@virginia.edu", "History")
        booklover.add_book("Fahrenheit 451", 2)
        booklover.add_book("Fahrenheit 451", 5)

        test = len(booklover.book_list[booklover.book_list["book_name"] == "Fahrenheit 451"])
        self.assertEqual(test, 1)

    def test_3_has_read(self):
        # pass a book in the list and test if the answer is `True`.
        booklover = BookLover("Terrance", "vwy4sa@virginia.edu", "History")
        booklover.add_book("The Great Gatsby", 3)
        
        self.assertTrue(booklover.has_read("The Great Gatsby"))

    def test_4_has_read(self):
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        booklover = BookLover("Terrance", "vwy4sa@virginia.edu", "History")

        self.assertFalse(booklover.has_read("DS 5100: Programming for Data Science"))

    def test_5_num_books_read(self):
        # add some books to the list, and test num_books matches expected.
        booklover = BookLover("Terrance", "vwy4sa@virginia.edu", "History")
        booklover.add_book("War and Peace", 3)
        booklover.add_book("The Catcher in the Rye", 5)
        booklover.add_book("The Lords of the Ring", 1)
        booklover.add_book("Invisible Man", 2)
        booklover.add_book("Frankenstein", 4)

        self.assertEqual(booklover.num_books_read(), 5)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3.
        # Your test should check that the returned books have rating  > 3
        booklover = BookLover("Terrance", "vwy4sa@virginia.edu", "History")

        booklover.add_book("Adventures of Huckleberry Finn", 4)
        booklover.add_book("To Kill a Mockingbird", 5)
        booklover.add_book("Moby-Dick", 1)
        booklover.add_book("Great Expectations", 2)
        booklover.add_book("Brave New World", 3)
        
        fav_books = booklover.fav_books()
        self.assertTrue("Adventures of Huckleberry Finn" in fav_books["book_name"].values)
        self.assertTrue("To Kill a Mockingbird" in fav_books["book_name"].values)
        self.assertFalse("Moby-Dick" in fav_books["book_name"].values)
        self.assertFalse("Great Expectations" in fav_books["book_name"].values)
        self.assertFalse("Brave New World" in fav_books["book_name"].values)
        
                                   
if __name__ == '__main__':
    unittest.main(verbosity=3)
        