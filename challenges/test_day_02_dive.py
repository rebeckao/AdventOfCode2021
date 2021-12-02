from unittest import TestCase

from challenges.day_02_dive import dive, dive_with_aim


class TestDive(TestCase):
    def test_dive(self):
        instructions = [
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2"
        ]
        horizontal, depth = dive(instructions)
        self.assertEqual(15, horizontal)
        self.assertEqual(10, depth)

    def test_dive_real_input(self):
        with open('inputs/day_02.txt') as f:
            instructions = f.readlines()
            horizontal, depth = dive(instructions)
            self.assertEqual(2011, horizontal)
            self.assertEqual(738, depth)

    def test_dive_with_aim(self):
        instructions = [
            "forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2"
        ]
        horizontal, depth = dive_with_aim(instructions)
        self.assertEqual(15, horizontal)
        self.assertEqual(60, depth)

    def test_dive_with_aim_real_input(self):
        with open('inputs/day_02.txt') as f:
            instructions = f.readlines()
            horizontal, depth = dive_with_aim(instructions)
            self.assertEqual(2011, horizontal)
            self.assertEqual(727910, depth)
