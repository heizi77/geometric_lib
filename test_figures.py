import math
import unittest

import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    """Тесты для circle.py: area(r) и perimeter(r)."""

    # --- area ---
    def test_area_example(self):
        self.assertAlmostEqual(circle.area(5), 78.53981633974483)

    def test_area_unit_radius(self):
        self.assertAlmostEqual(circle.area(1), math.pi)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_float_radius(self):
        self.assertAlmostEqual(circle.area(2.5), math.pi * 6.25)

    def test_area_scales_quadratically(self):
        self.assertAlmostEqual(circle.area(6), 4 * circle.area(3))

    def test_area_negative_radius(self):
        # Ожидаем, что отрицательный радиус отвергается
        with self.assertRaises(ValueError):
            circle.area(-3)

    def test_area_string_radius(self):
        with self.assertRaises(TypeError):
            circle.area("5")

    # --- perimeter ---
    def test_perimeter_example(self):
        self.assertAlmostEqual(circle.perimeter(5), 31.41592653589793)

    def test_perimeter_unit_radius(self):
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_float_radius(self):
        self.assertAlmostEqual(circle.perimeter(0.5), math.pi)

    def test_perimeter_negative_radius(self):
        with self.assertRaises(ValueError):
            circle.perimeter(-3)


class RectangleTestCase(unittest.TestCase):
    """Тесты для rectangle.py: area(a, b) и perimeter(a, b)."""

    # --- area ---
    def test_area_example(self):
        self.assertEqual(rectangle.area(3, 5), 15)

    def test_area_zero_side(self):
        self.assertEqual(rectangle.area(10, 0), 0)

    def test_area_square_case(self):
        self.assertEqual(rectangle.area(10, 10), 100)

    def test_area_float_sides(self):
        self.assertAlmostEqual(rectangle.area(2.5, 4), 10.0)

    def test_area_commutative(self):
        self.assertEqual(rectangle.area(3, 7), rectangle.area(7, 3))

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            rectangle.area(-3, 5)

    def test_area_string_and_number(self):
        # Строка и число не должны давать "площадь"
        with self.assertRaises(TypeError):
            rectangle.area("ab", 3)

    # --- perimeter ---
    def test_perimeter_example(self):
        self.assertEqual(rectangle.perimeter(3, 5), 16)

    def test_perimeter_zero_sides(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def test_perimeter_float_sides(self):
        self.assertAlmostEqual(rectangle.perimeter(2.5, 1.5), 8.0)

    def test_perimeter_commutative(self):
        self.assertEqual(rectangle.perimeter(3, 7), rectangle.perimeter(7, 3))

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            rectangle.perimeter(-3, 5)


class SquareTestCase(unittest.TestCase):
    """Тесты для square.py: area(a) и perimeter(a)."""

    # --- area ---
    def test_area_example(self):
        self.assertEqual(square.area(4), 16)

    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_float_side(self):
        self.assertAlmostEqual(square.area(1.5), 2.25)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            square.area(-4)

    def test_area_string_side(self):
        with self.assertRaises(TypeError):
            square.area("a")

    # --- perimeter ---
    def test_perimeter_example(self):
        self.assertEqual(square.perimeter(4), 16)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_float_side(self):
        self.assertAlmostEqual(square.perimeter(2.5), 10.0)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            square.perimeter(-4)

    def test_perimeter_string_side(self):
        with self.assertRaises(TypeError):
            square.perimeter("a")


class TriangleTestCase(unittest.TestCase):
    """Тесты для triangle.py: area(a, h) и perimeter(a, b, c)."""

    # --- area ---
    def test_area_example(self):
        self.assertEqual(triangle.area(4, 5), 10.0)

    def test_area_zero_base(self):
        self.assertEqual(triangle.area(0, 5), 0)

    def test_area_zero_height(self):
        self.assertEqual(triangle.area(5, 0), 0)

    def test_area_float_values(self):
        self.assertAlmostEqual(triangle.area(2.5, 4), 5.0)

    def test_area_negative_height(self):
        with self.assertRaises(ValueError):
            triangle.area(4, -5)

    # --- perimeter ---
    def test_perimeter_example(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)

    def test_perimeter_equilateral(self):
        self.assertEqual(triangle.perimeter(2, 2, 2), 6)

    def test_perimeter_zero_sides(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def test_perimeter_float_sides(self):
        self.assertAlmostEqual(triangle.perimeter(1.5, 2.5, 3.0), 7.0)

    def test_perimeter_order_independent(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), triangle.perimeter(5, 4, 3))

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            triangle.perimeter(-3, 4, 5)

    def test_perimeter_triangle_inequality(self):
        # Стороны 1, 1, 10 не образуют треугольник
        with self.assertRaises(ValueError):
            triangle.perimeter(1, 1, 10)


if __name__ == "__main__":
    unittest.main()