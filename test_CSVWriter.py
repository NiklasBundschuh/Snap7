import unittest
from CSVWriter import HeaderParser

class TestCSVWriter(unittest.TestCase):

    def test_HeaderParser(self):
        self.assertEqual(HeaderParser("Kopfzeilen START", []),["Kopfzeilen START\n"])
    
    def test_FooterParser(self):
        self.assertEqual(HeaderParser("Fusszeilen START", []),["Fusszeilen START\n"])

    def test_HeaderParser(self):
        self.assertEqual(HeaderParser("Zeittakt", []),["Zeittakt\n"])
    

if __name__ == '__main__':
    unittest.main()