import unittest
from PythonPersonalProject.Python.models import triangles


class TriangleTest(unittest.TestCase):
    def test_check_valid_number_0(self):
        self.assertEqual(triangles.check_valid_number(7), 7)

    def test_check_valid_number_1(self):
        self.assertEqual(triangles.check_valid_number(55), 55)

    def test_check_valid_number_2(self):
        self.assertEqual(triangles.check_valid_number(1), 1)

    def test_check_valid_number_3(self):
        self.assertEqual(triangles.check_valid_number(0), 0)

    def test_check_valid_number_4(self):
        self.assertEqual(triangles.check_valid_number('*'), 0)

    def test_check_valid_number_5(self):
        self.assertEqual(triangles.check_valid_number('number'), 0)

    def test_check_valid_number_6(self):
        self.assertEqual(triangles.check_valid_number(''), 0)

    def test_triangle_is_exist_0(self):
        self.assertTrue(triangles.triangle_is_exist(8, 8, 8))

    def test_triangle_is_exist_1(self):
        self.assertFalse(triangles.triangle_is_exist(0, 4, 0))

    def test_triangle_is_exist_2(self):
        self.assertFalse(triangles.triangle_is_exist(1, 92, 5))

    def test_check_valid_triangle_0(self):
        self.assertTrue(triangles.check_valid_triangle('first name', 3, 5, 6))

    def test_check_valid_triangle_1(self):
        self.assertTrue(triangles.check_valid_triangle('second name', 5, 5, 5))


if __name__ == '__main__':
    unittest.main()
