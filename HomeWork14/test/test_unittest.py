from task1 import Triangle
# from task1 import ErrorTriangle
# from task1 import ErrorSide
import unittest


class TestTriangle(unittest.TestCase):
    def setUp(self) -> None:
        self.t1 = Triangle(3, 6, 6)
        self.t2 = Triangle(5, 5, 5)
        self.t3 = Triangle(4, 5, 6)
        # self.t4 = Triangle(15, 5, 1)
        # self.t5 = Triangle(15, 5, -3)

    def test_get_isosceles(self):
        self.assertEqual(self.t1.check(), 'Треугольник - равнобедренный')

    def test_get_equilateral(self):
        self.assertEqual(self.t2.check(), 'Треугольник - равносторонний')

    def test_get_versatile(self):
        self.assertEqual(self.t3.check(), 'Треугольник - разносторонний')

    # def test_not_get_triangle(self):
    #     self.assertRaises(ErrorTriangle, self.t4.check())

    # def test_not_side_triangle(self):
    #     self.assertRaisesRegexp(
    #         ErrorSide, 'Стороны не могут принимать отрицательное значение:', self.t5)


if __name__ == '__main__':
    unittest.main(verbosity=10)
