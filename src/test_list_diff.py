from list_diff import ListDiff
import unittest


class ListDiffTest(unittest.TestCase):
    def test_calculate_diff(self):
        """Test diff between two lists"""
        list_1 = ['1', '2', '3']
        list_2 = ['1', '2']
        expected_diff = ['3']

        list_diff = ListDiff(list_1, list_2)
        result = list_diff.calculate_diff()

        self.assertEqual(result, expected_diff)


if __name__ == '__main__':
    unittest.main()
