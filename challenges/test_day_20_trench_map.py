from unittest import TestCase

from challenges.day_20_trench_map import lit_pixels_after_passes


class Test(TestCase):
    def test_lit_pixels_after_two_passes(self):
        iea = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##" \
              + "#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###" \
              + ".######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#." \
              + ".#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#....." \
              + ".#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.." \
              + "...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#....." \
              + "..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"
        input_image = [
            "#..#.",
            "#....",
            "##..#",
            "..#..",
            "..###"
        ]
        self.assertEqual(35, lit_pixels_after_passes(iea, input_image, 2))

    def test_lit_pixels_after_two_passes_real_input(self):
        with open('inputs/day_20.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(4873, lit_pixels_after_passes(lines[0], lines[2:], 2))

    def test_lit_pixels_after_fifty_passes(self):
        iea = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##" \
              + "#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###" \
              + ".######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#." \
              + ".#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#....." \
              + ".#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.." \
              + "...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#....." \
              + "..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"
        input_image = [
            "#..#.",
            "#....",
            "##..#",
            "..#..",
            "..###"
        ]
        self.assertEqual(3351, lit_pixels_after_passes(iea, input_image, 50))

    def test_lit_pixels_after_fifty_passes_real_input(self):
        with open('inputs/day_20.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(16394, lit_pixels_after_passes(lines[0], lines[2:], 50))
