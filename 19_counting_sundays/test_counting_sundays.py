import unittest
import counting_sundays
import archive
import datetime

class Test(unittest.TestCase):

    def test_datetime(self):
        self.assertEqual(datetime.datetime(2018, 10, 12).weekday(), 4)

    def test_start_next_month(self):
        self.assertEqual(archive.start_next_month((2018, 10, 25)), ((2018, 11, 1), 7))
        self.assertEqual(archive.start_next_month((2018, 12, 30)), ((2019, 1, 1), 2))
        self.assertEqual(archive.start_next_month((2018, 12, 1)), ((2018, 12, 1), 0))

    def test_leap_year(self):
        self.assertEqual(archive.leap_year(2000), True)
        self.assertEqual(archive.leap_year(1900), False)
        self.assertEqual(archive.leap_year(2004), True)
        self.assertEqual(archive.leap_year(1904), True)

    def test_next_month(self):
        self.assertEqual(counting_sundays.next_month((2018, 12, 1)), (2018, 12))
        self.assertEqual(counting_sundays.next_month((2018, 12, 30)), (2019, 1))
        self.assertEqual(counting_sundays.next_month((2018, 11, 20)), (2018, 12))

    def test_countint_sundays(self):
        self.assertEqual(archive.counting_sundays((1900, 1, 1), (1910, 1, 1)), 18)
        self.assertEqual(archive.counting_sundays((2000, 1, 1), (2020, 1, 1)), 35)

    def test_counting_sundays2(self):
        self.assertEqual(counting_sundays.counting_sundays((1900, 1, 1), (1910, 1, 1)), 18)
        self.assertEqual(counting_sundays.counting_sundays((2000, 1, 1), (2020, 1, 1)), 35)
        self.assertEqual(counting_sundays.counting_sundays((1900 + 2000, 1, 1), (1910 + 2000, 1, 1)), 18)
        self.assertEqual(counting_sundays.counting_sundays((1900 + 2800*357*10**10, 1, 1), (1910 + 2800*357*10**10, 1, 1)), 18)
        self.assertEqual(counting_sundays.counting_sundays((1900, 1, 1), (1900, 4, 1)), 1)
        self.assertEqual(counting_sundays.counting_sundays((1900, 4, 1), (1900, 4, 1)), 1)
        self.assertEqual(counting_sundays.counting_sundays((1900, 3, 2), (1900, 3, 3)), 0)
        self.assertEqual(counting_sundays.counting_sundays((4699, 12, 12), (4710, 1, 1)), 18)

    def test_Zeller(self):
        self.assertEqual(counting_sundays.Zeller(2018, 10, 12), datetime.datetime(2018, 10, 12).weekday())
        self.assertEqual(counting_sundays.Zeller(2000, 1, 1), datetime.datetime(2000, 1, 1).weekday())
        self.assertEqual(counting_sundays.Zeller(1900, 1, 1), datetime.datetime(1900, 1, 1).weekday())
        self.assertEqual(counting_sundays.Zeller(2400, 1, 1), datetime.datetime(2400, 1, 1).weekday())
        self.assertEqual(counting_sundays.Zeller(2401, 1, 1), datetime.datetime(2401, 1, 1).weekday())
        self.assertEqual(counting_sundays.Zeller(3650, 1, 1), datetime.datetime(3650, 1, 1).weekday())


if __name__ == '__main__':
    unittest.main()
