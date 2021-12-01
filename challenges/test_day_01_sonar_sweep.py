from unittest import TestCase

from challenges.day_01_sonar_sweep import number_of_increases, number_of_sliding_window_increases


class Test(TestCase):
    def test_number_of_increases(self):
        measurements = [199,
                        200,
                        208,
                        210,
                        200,
                        207,
                        240,
                        269,
                        260,
                        263]
        actual = number_of_increases(measurements)
        self.assertEqual(7, actual)

    def test_number_of_increases_real_input(self):
        with open('inputs/day_01.txt') as f:
            lines = f.readlines()
            measurements = [int(line) for line in lines]
            actual = number_of_increases(measurements)
            self.assertEqual(1557, actual)

    def test_number_of_sliding_window_increases(self):
        measurements = [199,
                        200,
                        208,
                        210,
                        200,
                        207,
                        240,
                        269,
                        260,
                        263]
        actual = number_of_sliding_window_increases(measurements)
        self.assertEqual(5, actual)

    def test_number_of_sliding_window_increases_real_input(self):
        with open('inputs/day_01.txt') as f:
            lines = f.readlines()
            measurements = [int(line) for line in lines]
            actual = number_of_sliding_window_increases(measurements)
            self.assertEqual(1608, actual)
