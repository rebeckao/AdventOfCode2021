from unittest import TestCase

from challenges.day_10_syntax_scoring import first_illegal_character, syntax_score, total_completion_score, middle_completion_score


class Test(TestCase):
    def test_first_illegal_character(self):
        self.assertEqual(None, first_illegal_character("[({(<(())[]>[[{[]{<()<>>"))
        self.assertEqual(None, first_illegal_character("[(()[<>])]({[<{<<[]>>("))
        self.assertEqual("}", first_illegal_character("{([(<{}[<>[]}>{[]{[(<()>"))
        self.assertEqual(None, first_illegal_character("(((({<>}<{<{<>}{[]{[]{}"))
        self.assertEqual(")", first_illegal_character("[[<[([]))<([[{}[[()]]]"))
        self.assertEqual("]", first_illegal_character("[{[{({}]{}}([{[{{{}}([]"))
        self.assertEqual(None, first_illegal_character("{<[[]]>}<{[{[{[]{()[[[]"))
        self.assertEqual(")", first_illegal_character("[<(<(<(<{}))><([]([]()"))
        self.assertEqual(">", first_illegal_character("<{([([[(<>()){}]>(<<{{"))
        self.assertEqual(None, first_illegal_character("<{([{{}}[<[[[<>{}]]]>[]]"))

    def test_syntax_score(self):
        actual = syntax_score([
            "[({(<(())[]>[[{[]{<()<>>",
            "[(()[<>])]({[<{<<[]>>(",
            "{([(<{}[<>[]}>{[]{[(<()>",
            "(((({<>}<{<{<>}{[]{[]{}",
            "[[<[([]))<([[{}[[()]]]",
            "[{[{({}]{}}([{[{{{}}([]",
            "{<[[]]>}<{[{[{[]{()[[[]",
            "[<(<(<(<{}))><([]([]()",
            "<{([([[(<>()){}]>(<<{{",
            "<{([{{}}[<[[[<>{}]]]>[]]"
        ])
        self.assertEqual(26397, actual)

    def test_syntax_score_real_input(self):
        with open('inputs/day_10.txt') as f:
            lines = f.read().splitlines()
            actual = syntax_score(lines)
            self.assertEqual(364389, actual)

    def test_completion_score(self):
        self.assertEqual(288957, total_completion_score("[({(<(())[]>[[{[]{<()<>>"))
        self.assertEqual(5566, total_completion_score("[(()[<>])]({[<{<<[]>>("))
        self.assertEqual(1480781, total_completion_score("(((({<>}<{<{<>}{[]{[]{}"))
        self.assertEqual(995444, total_completion_score("{<[[]]>}<{[{[{[]{()[[[]"))
        self.assertEqual(294, total_completion_score("<{([{{}}[<[[[<>{}]]]>[]]"))

    def test_middle_completion_score(self):
        actual = middle_completion_score([
            "[({(<(())[]>[[{[]{<()<>>",
            "[(()[<>])]({[<{<<[]>>(",
            "{([(<{}[<>[]}>{[]{[(<()>",
            "(((({<>}<{<{<>}{[]{[]{}",
            "[[<[([]))<([[{}[[()]]]",
            "[{[{({}]{}}([{[{{{}}([]",
            "{<[[]]>}<{[{[{[]{()[[[]",
            "[<(<(<(<{}))><([]([]()",
            "<{([([[(<>()){}]>(<<{{",
            "<{([{{}}[<[[[<>{}]]]>[]]"
        ])
        self.assertEqual(288957, actual)

    def test_middle_completion_score_real_input(self):
        with open('inputs/day_10.txt') as f:
            lines = f.read().splitlines()
            actual = middle_completion_score(lines)
            self.assertEqual(2870201088, actual)
