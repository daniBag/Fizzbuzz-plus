from fizzbuzz_plus import fizzbuzz
import unittest

correct_result = ["1", "Prime", "Prime", "4", "Prime", "Fizz", "Prime", "8", "Fizz", "Buzz", "Prime", "Fizz", "Prime", "14", "Fizzbuzz", "16", "Prime", "Fizz", "Prime", "Buzz"]

class TestFizzbuzzPlus(unittest.TestCase):

    def test_prints(self):
        self.assertEqual(fizzbuzz(1, 20), correct_result)

    def test_reversed_range(self):
        self.assertEqual(correct_result, fizzbuzz(20, 1))

    def test_edge_cases(self):
        self.assertEqual(fizzbuzz(25, 25), ["Buzz"])
        self.assertEqual(fizzbuzz(49, 49), ["49"])

    def test_single_number_cases(self):
        self.assertEqual(fizzbuzz(3, 3), ["Prime"])
        self.assertEqual(fizzbuzz(15, 15), ["Fizzbuzz"])