from unittest import TestCase

from challenges.day_17_trick_shot import highest_y


class Test(TestCase):
    def test_highest_y(self):
        self.assertEqual(45, highest_y(-10))

    def test_highest_y_real_input(self):
        self.assertEqual(6441, highest_y(-114))
