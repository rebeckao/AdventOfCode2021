from unittest import TestCase

from challenges.day_21_dirac_dice import dirac_dice, mod_position, dirac_quantum_dice


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

    def test_quantum_dirac_dice(self):
        player1_wins, player2_wins = dirac_quantum_dice(4, 8)
        self.assertEqual(444356092776315, player1_wins)
        self.assertEqual(341960390180808, player2_wins)

    def test_quantum_dirac_dice_real_input(self):
        player1_wins, player2_wins = dirac_quantum_dice(7, 9)
        self.assertEqual(433315766324816, player1_wins)
        self.assertEqual(353242407657025, player2_wins)
