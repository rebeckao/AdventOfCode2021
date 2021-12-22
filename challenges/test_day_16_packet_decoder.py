from unittest import TestCase

from challenges.day_16_packet_decoder import hexadecimal_to_binary, to_decimal, sum_of_version_numbers


class Test(TestCase):
    def test_hexadecimal_to_binary(self):
        actual = "".join([str(digit) for digit in hexadecimal_to_binary("D2FE28")])
        self.assertEqual("110100101111111000101000", actual)

    def test_to_decimal(self):
        self.assertEqual(4, to_decimal([1, 0, 0]))
        self.assertEqual(2021, to_decimal([0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1]))

    def test_sum_of_version_numbers(self):
        self.assertEqual(6, sum_of_version_numbers("D2FE28"))
        self.assertEqual(1 + 6 + 2, sum_of_version_numbers("38006F45291200"))
        self.assertEqual(4 + 1 + 5 + 6, sum_of_version_numbers("8A004A801A8002F478"))
        self.assertEqual(12, sum_of_version_numbers("620080001611562C8802118E34"))
        self.assertEqual(23, sum_of_version_numbers("C0015000016115A2E0802F182340"))
        self.assertEqual(31, sum_of_version_numbers("A0016C880162017C3686B18A3D4780"))

    def test_sum_of_version_numbers_real_input(self):
        with open('inputs/day_16.txt') as f:
            hexadecimal = f.read().splitlines()[0]
            self.assertEqual(883, sum_of_version_numbers(hexadecimal))
