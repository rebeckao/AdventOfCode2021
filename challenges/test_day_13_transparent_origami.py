from unittest import TestCase

from challenges.day_13_transparent_origami import visible_after_fold


class Test(TestCase):
    def test_visible_after_fold(self):
        self.assertEqual(17, visible_after_fold([
            "6,10",
            "0,14",
            "9,10",
            "0,3",
            "10,4",
            "4,11",
            "6,0",
            "6,12",
            "4,1",
            "0,13",
            "10,12",
            "3,4",
            "3,0",
            "8,4",
            "1,10",
            "2,14",
            "8,10",
            "9,0"
        ], "fold along y=7"))

    def test_visible_after_fold_real_input(self):
        with open('inputs/day_13.txt') as f:
            all_lines = f.read().splitlines()
            empty_line = all_lines.index("")
            points = all_lines[0:empty_line]
            fold_instructions = all_lines[empty_line + 1:]
            self.assertEqual(666, visible_after_fold(points, fold_instructions[0]))
