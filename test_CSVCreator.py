import unittest
from CSVCreator import ReadAndWrite

class TestCSVCreator(unittest.TestCase):

    def test_ReadAndWriter(self):
        self.assertEqual(ReadAndWrite("Kopfzeilen START"),"Kopfzeilen START;\n")



if __name__ == '__main__':
    unittest.main()