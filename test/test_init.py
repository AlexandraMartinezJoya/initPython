import unittest


class TotalSumTest(unittest.TestCase):

    def test_list_init(self):
        """
        Test that init sums up a total of integers
        :return: int total sum
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertIs(result, 6)
