import data
import lab4
import unittest



# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)

    def test_first_element_2(self):
        # write a second test here
        input = [[5,6], [4,2,8]]
        result = lab4.first_element(input)
        expected = [5,4]
        self.assertEqual(expected,result)

    # Part 2
    def test_x_coordinates_1(self):
        point_a = data.Point(5,7)
        point_b = data.Point(90,6)
        input = [point_a, point_b]
        result = lab4.x_coordinates(input)
        expected = [5,90]
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        point_a = data.Point(10,30)
        point_b = data.Point(25,78)
        point_c = data.Point(58, 8)
        input = [point_a, point_b, point_c]
        result = lab4.x_coordinates(input)
        expected = [10,25,58]
        self.assertEqual(expected, result)

    # Part 3
    def test_are_in_positive_quadrant_1(self):
        point_a = data.Point(5, 7)
        point_b = data.Point(-90, 6)
        point_c = data.Point(2,1)
        input = [point_a, point_b, point_c]
        result = lab4.are_in_positive_quadrant(input)
        expected = [point_a, point_c]
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant_2(self):
        point_a = data.Point(-10,-30)
        point_b = data.Point(25,78)
        point_c = data.Point(0, -8)
        input = [point_a, point_b, point_c]
        result = lab4.are_in_positive_quadrant(input)
        expected = [point_b]
        self.assertEqual(expected, result)

    # Part 4
    def test_distance_1(self):
        a = data.Point(20,30)
        b = data.Point(5, 15)
        result = lab4.distance(a,b)
        expected = 21.21
        self.assertAlmostEqual(result, expected, 2)

    def test_distance_2(self):
        a = data.Point(-17, 2)
        b = data.Point(3, 8.2)
        result = lab4.distance(a,b)
        expected = 20.94
        self.assertAlmostEqual(result, expected, 2)

    # Part 5
    def test_manhattan_distance_1(self):
        a = data.Point(7.6, -10)
        b = data.Point(-5.6, 9.7)
        result = lab4.manhattan_distance(a,b)
        expected = 32.9
        self.assertEqual(result, expected)

    def test_manhattan_distance_2(self):
        a = data.Point(3.4, 80)
        b = data.Point(-3.4, -80)
        result = lab4.manhattan_distance(a,b)
        expected = 166.8
        self.assertEqual(result, expected)

# Part 6
    def test_distance_all_1(self):
        a = data.Point(6.9, 69)
        b = data.Point(-30.7, -80.1)
        input = [a,b]
        result = lab4.distance_all(input)
        expected = [75.9, 110.8]
        self.assertEqual(result, expected)

    def test_distance_all_2(self):
        a = data.Point(14.1, -54.7)
        b = data.Point(7, 9)
        c = data.Point(4.6, -9.8)
        input = [a,b,c]
        result = lab4.distance_all(input)
        expected = [68.8,16,14.4]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
