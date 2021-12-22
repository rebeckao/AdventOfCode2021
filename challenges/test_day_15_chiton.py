from unittest import TestCase

from challenges.day_15_chiton import lowest_risk_breath_first


class Test(TestCase):
    def test_lowest_risk(self):
        self.assertEqual(5, lowest_risk_breath_first([
            "121",
            "131",
            "151",
        ]))
        self.assertEqual(38, lowest_risk_breath_first([
            "1163751742",
            "1381373672"
        ]))
        self.assertEqual(12, lowest_risk_breath_first([
            "11199",
            "99199",
            "11199",
            "19999",
            "11111",
        ]))
        self.assertEqual(14, lowest_risk_breath_first([
            "111999",
            "991999",
            "111999",
            "199999",
            "199999",
            "111111",
        ]))
        self.assertEqual(19, lowest_risk_breath_first([
            "111199",
            "999199",
            "111199",
            "199999",
            "191111",
            "191991",
            "111991"
        ]))
        self.assertEqual(40, lowest_risk_breath_first([
            "1163751742",
            "1381373672",
            "2136511328",
            "3694931569",
            "7463417111",
            "1319128137",
            "1359912421",
            "3125421639",
            "1293138521",
            "2311944581"
        ]))

    def test_lowest_risk_real_input(self):
        with open('inputs/day_15.txt') as f:
            all_lines = f.read().splitlines()
            self.assertEqual(19, lowest_risk_breath_first(all_lines))
