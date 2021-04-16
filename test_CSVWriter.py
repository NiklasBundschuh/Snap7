import unittest
from CSVWriter import HeaderParser

class TestCSVWriter(unittest.TestCase):

    def test_HeaderParser(self):
        self.assertEqual(HeaderParser("Kopfzeilen START", []),["Kopfzeilen START\n"])
    
if __name__ == '__main__':
    unittest.main()