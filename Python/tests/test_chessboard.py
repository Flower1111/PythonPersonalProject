import unittest
from PythonPersonalProject.Python.models import chessboard


class ChessTest(unittest.TestCase):
    def test_check_valid_number_0(self):
        self.assertEqual(chessboard.check_valid_number(8), 8)

    def test_check_valid_number_1(self):
        self.assertEqual(chessboard.check_valid_number(67), 67)

    def test_check_valid_number_2(self):
        self.assertEqual(chessboard.check_valid_number(0), 0)

    def test_check_valid_number_3(self):
        self.assertEqual(chessboard.check_valid_number(1), 1)

    def test_check_valid_number_4(self):
        self.assertEqual(chessboard.check_valid_number('*'), 0)

    def test_check_valid_number_5(self):
        self.assertEqual(chessboard.check_valid_number('one'), 0)

    def test_check_valid_number_6(self):
        self.assertEqual(chessboard.check_valid_number(''), 0)


if __name__ == '__main__':
    unittest.main()
