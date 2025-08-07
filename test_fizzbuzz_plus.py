from fizzbuzz_plus import fizzbuzz
import unittest

correct_result = ["1", "Prime", "Prime", "4", "Prime", "Fizz", "Prime", "8", "Fizz", "Buzz", "Prime", "Fizz", "Prime", "14", "Fizzbuzz", "16", "Prime", "Fizz", "Prime", "Buzz"]

class TestNumsDivision(unittest.TestCase):

    def test_prints(self):
        result = fizzbuzz(1, 20)
        self.assertEqual(result, correct_result)

    def test_reversed_range(self):
        assert correct_result == fizzbuzz(20, 1)

    def test_edge_cases(self):
        assert fizzbuzz(25, 25) == ["25"]
        assert fizzbuzz(49, 49) == ["49"]

    def test_single_number_cases(self):
        assert fizzbuzz(3,3) == ["Prime"]
        assert fizzbuzz(15,15) == ["Fizzbuzz"]