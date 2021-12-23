from unittest import TestCase

from challenges.day_17_trick_shot import highest_y, number_of_different_velocities_landing_in_target, reaches_goal


class Test(TestCase):
    def test_highest_y(self):
        self.assertEqual(45, highest_y(-10))

    def test_highest_y_real_input(self):
        self.assertEqual(6441, highest_y(-114))

    def test_number_of_different_velocities_landing_in_target(self):
        self.assertEqual(112, number_of_different_velocities_landing_in_target(20, 30, -10, -5))

    def test_number_of_different_velocities_landing_in_target_real_input(self):
        self.assertEqual(3186, number_of_different_velocities_landing_in_target(153, 199, -114, -75))

    def test_reaches_goal(self):
        self.assertEqual(True, reaches_goal(20, 30, -10, -5, 26, -10))
        self.assertEqual(True, reaches_goal(20, 30, -10, -5, 10, -2))
        self.assertEqual(True, reaches_goal(20, 30, -10, -5, 6, 6))
        self.assertEqual(False, reaches_goal(20, 30, -10, -5, 6, -10))
        self.assertEqual(False, reaches_goal(20, 30, -10, -5, 10, 6))
