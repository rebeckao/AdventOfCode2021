from unittest import TestCase

from challenges.day_11_dumbo_octopus import total_flashes_after_steps, first_step_when_all_flash_together


class Test(TestCase):
    def test_total_flashes_after_steps(self):
        self.assertEqual(9, total_flashes_after_steps([
            "11111",
            "19991",
            "19191",
            "19991",
            "11111"
        ], 2))
        self.assertEqual(204, total_flashes_after_steps([
            "5483143223",
            "2745854711",
            "5264556173",
            "6141336146",
            "6357385478",
            "4167524645",
            "2176841721",
            "6882881134",
            "4846848554",
            "5283751526"
        ], 10))
        self.assertEqual(1656, total_flashes_after_steps([
            "5483143223",
            "2745854711",
            "5264556173",
            "6141336146",
            "6357385478",
            "4167524645",
            "2176841721",
            "6882881134",
            "4846848554",
            "5283751526"
        ], 100))

    def test_total_flashes_after_steps_real_input(self):
        with open('inputs/day_11.txt') as f:
            octopuses = f.read().splitlines()
            self.assertEqual(1757, total_flashes_after_steps(octopuses, 100))

    def test_first_step_when_all_flash_together(self):
        self.assertEqual(195, first_step_when_all_flash_together([
            "5483143223",
            "2745854711",
            "5264556173",
            "6141336146",
            "6357385478",
            "4167524645",
            "2176841721",
            "6882881134",
            "4846848554",
            "5283751526"
        ]))

    def test_first_step_when_all_flash_together_real_input(self):
        with open('inputs/day_11.txt') as f:
            octopuses = f.read().splitlines()
            self.assertEqual(422, first_step_when_all_flash_together(octopuses))
