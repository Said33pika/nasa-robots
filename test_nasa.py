import unittest
from nasa import left, right, move, validate_parts, validate_instructions
import nasa
nasa.ur_coords_x = 5
nasa.ur_coords_y = 5

class TestRobotNavigation(unittest.TestCase):

    def test_left_rotation(self):
        self.assertEqual(left(1, 2, 'N'), (1, 2, 'W'))
        self.assertEqual(left(3, 4, 'W'), (3, 4, 'S'))
        self.assertEqual(left(0, 2, 'S'), (0, 2, 'E'))
        self.assertEqual(left(2, 2, 'E'), (2, 2, 'N'))

    def test_right_rotation(self):
        self.assertEqual(right(5, 2, 'N'), (5, 2, 'E'))
        self.assertEqual(right(1, 3, 'E'), (1, 3, 'S'))
        self.assertEqual(right(4, 2, 'S'), (4, 2, 'W'))
        self.assertEqual(right(1, 5, 'W'), (1, 5, 'N'))

    def test_move_within_bounds(self):
        self.assertEqual(move(1, 2, 'N'), (1, 3, 'N'))
        self.assertEqual(move(0, 0, 'E'), (1, 0, 'E'))
        self.assertEqual(move(3, 2, 'S'), (3, 1, 'S'))
        self.assertEqual(move(1, 5, 'W'), (0, 5, 'W'))

    def test_move_out_of_bounds(self):
        self.assertEqual(move(0, 1, 'S'), (0, 0, 'S'))
        self.assertEqual(move(0, 0, 'W'), (0, 0, 'W'))
        self.assertEqual(move(4, 5, 'N'), (4, 5, 'N'))
        self.assertEqual(move(5, 4, 'E'), (5, 4, 'E'))

    def test_validate_parts_valid(self):
        self.assertTrue(validate_parts(['1', '2', 'N']))
        self.assertTrue(validate_parts(['5', '5', 'E']))

    def test_validate_parts_invalid(self):
        self.assertFalse(validate_parts(['1', '2']))  # missing direction
        self.assertFalse(validate_parts(['a', '2', 'N']))  # non-numeric x
        self.assertFalse(validate_parts(['1', 'b', 'E']))  # non-numeric y
        self.assertFalse(validate_parts(['1', '2', 'Q']))  # invalid direction
        self.assertFalse(validate_parts(['6', '2', 'N']))  # x out of bounds
        self.assertFalse(validate_parts(['2', '6', 'S']))  # y out of bounds

    def test_validate_instructions_valid(self):
        self.assertTrue(validate_instructions('LMLMRM'))
        self.assertTrue(validate_instructions('lrmLRM'))  # case insensitive

    def test_validate_instructions_invalid(self):
        self.assertFalse(validate_instructions('ABCM'))
        self.assertFalse(validate_instructions('123'))
        self.assertFalse(validate_instructions('LMR!@#'))

if __name__ == '__main__':
    unittest.main()
