from unittest.mock import patch

from fizzbuzz_plus import fizzbuzz
from io import StringIO
import unittest

correct_result = ["1", "prime", "prime", "4", "prime", "fizz", "prime", "8", "fizz", "buzz", "prime", "fizz", "prime", "14", "fizzbuzz", "16", "prime", "fizz", "prime", "buzz"]

class TestNumsDivision(unittest.TestCase):

    def test_prints(self):
        result = fizzbuzz(1, 20)
        self.assertEqual(result, correct_result)