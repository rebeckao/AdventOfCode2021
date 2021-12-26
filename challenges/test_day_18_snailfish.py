from unittest import TestCase

from challenges.day_18_snailfish import add_together_list, reduce_one_step, reduce, magnitude, parse_snailfish_expression, largest_magnitude


class Test(TestCase):
    def test_magnitude(self):
        self.assertEqual(29, magnitude(parse_snailfish_expression("[9,1]")))
        self.assertEqual(129, magnitude(parse_snailfish_expression("[[9,1],[1,9]]")))
        self.assertEqual(1384, magnitude(parse_snailfish_expression("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")))
        self.assertEqual(445, magnitude(parse_snailfish_expression("[[[[1,1],[2,2]],[3,3]],[4,4]]")))
        self.assertEqual(1137, magnitude(parse_snailfish_expression("[[[[5,0],[7,4]],[5,5]],[6,6]]")))
        self.assertEqual(3488, magnitude(parse_snailfish_expression("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]")))

    def test_add_together_list(self):
        self.assertEqual("[[1,2],[[3,4],5]]", add_together_list([
            "[1,2]",
            "[[3,4],5]"
        ]))
        self.assertEqual("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", add_together_list([
            "[[[[4,3],4],4],[7,[[8,4],9]]]",
            "[1,1]"
        ]))
        self.assertEqual("[[[[1,1],[2,2]],[3,3]],[4,4]]", add_together_list([
            "[1,1]",
            "[2,2]",
            "[3,3]",
            "[4,4]"
        ]))
        self.assertEqual("[[[[3,0],[5,3]],[4,4]],[5,5]]", add_together_list([
            "[1,1]",
            "[2,2]",
            "[3,3]",
            "[4,4]",
            "[5,5]"
        ]))
        self.assertEqual("[[[[5,0],[7,4]],[5,5]],[6,6]]", add_together_list([
            "[1,1]",
            "[2,2]",
            "[3,3]",
            "[4,4]",
            "[5,5]",
            "[6,6]"
        ]))
        self.assertEqual("[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]", add_together_list([
            "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
            "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]"
        ]))
        self.assertEqual("[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]", add_together_list([
            "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
            "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
            "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
            "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]",
            "[7,[5,[[3,8],[1,4]]]]",
            "[[2,[2,2]],[8,[8,1]]]",
            "[2,9]",
            "[1,[[[9,3],9],[[9,0],[0,7]]]]",
            "[[[5,[7,4]],7],1]",
            "[[[[4,2],2],6],[8,7]]"
        ]))
        self.assertEqual("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]", add_together_list([
            "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
            "[[[5,[2,8]],4],[5,[[9,9],0]]]",
            "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
            "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
            "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
            "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
            "[[[[5,4],[7,7]],8],[[8,3],8]]",
            "[[9,3],[[9,9],[6,[4,9]]]]",
            "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
            "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"
        ]))

    def test_single_reduce_step(self):
        self.assertEqual("[[[[0,9],2],3],4]", reduce_one_step("[[[[[9,8],1],2],3],4]"))
        self.assertEqual("[[[[0,7],4],[7,[[8,4],9]]],[1,1]]", reduce_one_step("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"))
        self.assertEqual("[7,[6,[5,[7,0]]]]", reduce_one_step("[7,[6,[5,[4,[3,2]]]]]"))
        self.assertEqual("[[6,[5,[7,0]]],3]", reduce_one_step("[[6,[5,[4,[3,2]]]],1]"))
        self.assertEqual("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", reduce_one_step("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]"))
        self.assertEqual("[[3,[2,[8,0]]],[9,[5,[7,0]]]]", reduce_one_step("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"))
        self.assertEqual("[[[[0,7],4],[15,[0,13]]],[1,1]]", reduce_one_step("[[[[0,7],4],[7,[[8,4],9]]],[1,1]]"))
        self.assertEqual("[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]", reduce_one_step("[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]"))
        self.assertEqual("[[[5,[2,8]],4],[5,[[9,9],0]]]", reduce_one_step("[[[5,[2,8]],4],[5,[[9,9],0]]]"))
        self.assertEqual("[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]", reduce_one_step("[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]"))
        self.assertEqual("[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]", reduce_one_step("[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]"))
        self.assertEqual("[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]", reduce_one_step("[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]"))
        self.assertEqual("[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]", reduce_one_step("[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]"))
        self.assertEqual("[[[[5,4],[7,7]],8],[[8,3],8]]", reduce_one_step("[[[[5,4],[7,7]],8],[[8,3],8]]"))
        self.assertEqual("[[9,3],[[9,9],[6,[4,9]]]]", reduce_one_step("[[9,3],[[9,9],[6,[4,9]]]]"))
        self.assertEqual("[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]", reduce_one_step("[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]"))
        self.assertEqual("[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]", reduce_one_step("[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"))

    def test_reduce(self):
        self.assertEqual("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]", reduce("[[[[[7,7],[7,7]],[[7,7],[7,7]]],[[[8,7],[8,7]],[[7,9],[5,0]]]],[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]]"))

    def test_add_together_list_real_input(self):
        with open('inputs/day_18.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(4243, magnitude(parse_snailfish_expression(add_together_list(lines))))

    def test_largest_magnitude(self):
        self.assertEqual(3993, largest_magnitude([
            "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
            "[[[5,[2,8]],4],[5,[[9,9],0]]]",
            "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
            "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
            "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
            "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
            "[[[[5,4],[7,7]],8],[[8,3],8]]",
            "[[9,3],[[9,9],[6,[4,9]]]]",
            "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
            "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"
        ]))

    def test_largest_magnitude_real_input(self):
        with open('inputs/day_18.txt') as f:
            lines = f.read().splitlines()
            self.assertEqual(4701, largest_magnitude(lines))
