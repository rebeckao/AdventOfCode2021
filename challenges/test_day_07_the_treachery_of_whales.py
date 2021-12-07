from unittest import TestCase

from challenges.day_07_the_treachery_of_whales import most_fuel_efficient_position, linear_cost_of_position, \
    growing_cost_of_position


class Test(TestCase):
    def test_most_fuel_efficient_position_linear(self):
        actual_position, actual_cost = most_fuel_efficient_position([16, 1, 2, 0, 4, 2, 7, 1, 2, 14],
                                                                    linear_cost_of_position)
        self.assertEqual(2, actual_position)
        self.assertEqual(37, actual_cost)

    def test_linear_cost_of_position(self):
        initial_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        self.assertEqual(37, linear_cost_of_position(initial_positions, 2))
        self.assertEqual(41, linear_cost_of_position(initial_positions, 1))
        self.assertEqual(39, linear_cost_of_position(initial_positions, 3))
        self.assertEqual(71, linear_cost_of_position(initial_positions, 10))

    def test_most_fuel_efficient_position_linear_real_input(self):
        with open('inputs/day_07.txt') as f:
            numbers = [int(number) for number in f.read().splitlines()[0].split(",")]
            actual_position, actual_cost = most_fuel_efficient_position(numbers, linear_cost_of_position)
            self.assertEqual(372, actual_position)
            self.assertEqual(337488, actual_cost)

    def test_most_fuel_efficient_position_growing(self):
        actual_position, actual_cost = most_fuel_efficient_position([16, 1, 2, 0, 4, 2, 7, 1, 2, 14],
                                                                    growing_cost_of_position)
        self.assertEqual(5, actual_position)
        self.assertEqual(168, actual_cost)

    def test_growing_cost_of_position(self):
        initial_positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        self.assertEqual(206, growing_cost_of_position(initial_positions, 2))
        self.assertEqual(168, growing_cost_of_position(initial_positions, 5))

    def test_most_fuel_efficient_position_growing_real_input(self):
        with open('inputs/day_07.txt') as f:
            numbers = [int(number) for number in f.read().splitlines()[0].split(",")]
            actual_position, actual_cost = most_fuel_efficient_position(numbers, growing_cost_of_position)
            self.assertEqual(480, actual_position)
            self.assertEqual(89647695, actual_cost)
