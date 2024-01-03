import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("upper case".upper(), "UPPER CASE")\
    
    def test_isupper(self):
        self.assertTrue("UPPER CASE".isupper())
        self.assertFalse("not upper case".isupper())

    def test_split(self):
        w = "Bye World!"
        self.assertEqual(w.split(), ['Bye', 'World']) # it will output fail and error!
        with self.assertRaises(TypeError):
            w.split(2)


if __name__ == "__main__":
    unittest.main()
