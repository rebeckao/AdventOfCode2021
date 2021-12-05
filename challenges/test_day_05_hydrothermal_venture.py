from unittest import TestCase

from challenges.day_05_hydrothermal_venture import number_of_intersections_excluding_diagonal, \
    number_of_intersections_including_diagonal


class Test(TestCase):
    def test_number_of_intersections(self):
        vent_lines = [
            "0,9 -> 5,9",
            "8,0 -> 0,8",
            "9,4 -> 3,4",
            "2,2 -> 2,1",
            "7,0 -> 7,4",
            "6,4 -> 2,0",
            "0,9 -> 2,9",
            "3,4 -> 1,4",
            "0,0 -> 8,8",
            "5,5 -> 8,2"
        ]
        actual = number_of_intersections_excluding_diagonal(vent_lines)
        self.assertEqual(5, actual)

    def test_number_of_intersections_real_input(self):
        with open('inputs/day_05.txt') as f:
            vent_lines = f.read().splitlines()
            actual = number_of_intersections_excluding_diagonal(vent_lines)
            self.assertEqual(5169, actual)

    def test_number_of_intersections_including_diagonal(self):
        vent_lines = [
            "0,9 -> 5,9",
            "8,0 -> 0,8",
            "9,4 -> 3,4",
            "2,2 -> 2,1",
            "7,0 -> 7,4",
            "6,4 -> 2,0",
            "0,9 -> 2,9",
            "3,4 -> 1,4",
            "0,0 -> 8,8",
            "5,5 -> 8,2"
        ]
        actual = number_of_intersections_including_diagonal(vent_lines)
        self.assertEqual(12, actual)

    def test_number_of_intersections_including_diagonal_real_input(self):
        with open('inputs/day_05.txt') as f:
            vent_lines = f.read().splitlines()
            actual = number_of_intersections_including_diagonal(vent_lines)
            self.assertEqual(22083, actual)
