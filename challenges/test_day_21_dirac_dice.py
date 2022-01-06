from unittest import TestCase

from challenges.day_21_dirac_dice import dirac_dice, mod_position


class Test(TestCase):
    def test_dirac_dice(self):
        die_rolls, losing_score = dirac_dice(4, 8)
        self.assertEqual(739785, die_rolls * losing_score)

    def test_dirac_dice_real_input(self):
        die_rolls, losing_score = dirac_dice(7, 9)
        self.assertEqual(679329, die_rolls * losing_score)

    def test_mod_position(self):
        self.assertEqual(1, mod_position(1))
        self.assertEqual(10, mod_position(10))
        self.assertEqual(1, mod_position(11))
