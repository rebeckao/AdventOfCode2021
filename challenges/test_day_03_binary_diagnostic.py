from unittest import TestCase

from challenges.day_03_binary_diagnostic import power_consumption


class Test(TestCase):
    def test_power_consumption(self):
        diagnostic = [
            "00100",
            "11110",
            "10110",
            "10111",
            "10101",
            "01111",
            "00111",
            "11100",
            "10000",
            "11001",
            "00010",
            "01010"
        ]
        gamma_rate, epsilon_rate = power_consumption(diagnostic)
        self.assertEqual(22, gamma_rate)
        self.assertEqual(9, epsilon_rate)
        self.assertEqual(198, gamma_rate * epsilon_rate)

    def test_power_consumption_real_input(self):
        with open('inputs/day_03.txt') as f:
            diagnostic = f.read().splitlines()
            gamma_rate, epsilon_rate = power_consumption(diagnostic)
            self.assertEqual(1300, gamma_rate)
            self.assertEqual(2795, epsilon_rate)
            self.assertEqual(3633500, gamma_rate * epsilon_rate)  # 14536600 too high
