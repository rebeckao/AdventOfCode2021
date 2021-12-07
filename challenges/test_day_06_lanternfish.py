from unittest import TestCase

from challenges.day_06_lanternfish import fish_after_days


class Test(TestCase):
    def test_fish_after_days(self):
        self.assertEqual(26, fish_after_days("3,4,3,1,2", 18))
        self.assertEqual(5934, fish_after_days("3,4,3,1,2", 80))
        self.assertEqual(26984457539, fish_after_days("3,4,3,1,2", 256))

    def test_fish_after_days_real_input(self):
        with open('inputs/day_06.txt') as f:
            initial_fish = f.read().splitlines()[0]
            self.assertEqual(379414, fish_after_days(initial_fish, 80))
            self.assertEqual(1705008653296, fish_after_days(initial_fish, 256))
