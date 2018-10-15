import unittest
import n_digit_fibonacci_number

class Test(unittest.TestCase):

    def test_n_digit_fibonacci_number(self):
        self.assertEqual(n_digit_fibonacci_number.n_digit_fibonacci_number(3), 12)
        print(n_digit_fibonacci_number.n_digit_fibonacci_number(5000))

    def test_n_digit_fibonacci_number(self):
        #self.assertEqual(n_digit_fibonacci_number.n_digit_fibonacci_number2(3), 12)
        print(n_digit_fibonacci_number.n_digit_fibonacci_number2(5000))


if __name__ == '__main__':
    unittest.main()
