from unittest import TestCase

from challenges.day_09_smoke_basin import risk_scores_of_local_minima, basin_sizes


class Test(TestCase):
    def test_risk_scores_of_local_minima(self):
        actual = risk_scores_of_local_minima([
            "2199943210",
            "3987894921",
            "9856789892",
            "8767896789",
            "9899965678"
        ])
        self.assertEqual(15, actual)

    def test_risk_scores_of_local_minima_real_input(self):
        with open('inputs/day_09.txt') as f:
            cave_map = f.read().splitlines()
            actual = risk_scores_of_local_minima(cave_map)
            self.assertEqual(560, actual)

    def test_basin_sizes(self):
        actual = basin_sizes([
            "2199943210",
            "3987894921",
            "9856789892",
            "8767896789",
            "9899965678"
        ])
        self.assertEqual(1134, actual)

    def test_basin_sizes_real_input(self):
        with open('inputs/day_09.txt') as f:
            cave_map = f.read().splitlines()
            actual = basin_sizes(cave_map)
            self.assertEqual(959136, actual)
