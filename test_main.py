from lib2to3.pytree import convert
from unittest import TestCase
from main import Roman

class TestRoman(TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.instance = Roman()

    def test_1_to_I_roman(self):
        arabic = 1
        roman = 'I'
        converted = self.instance.convert(arabic)
        self.assertEqual(roman, converted)

    def test_2_to_II_roman(self):
        arabic = 2
        roman = 'II'
        converted = self.instance.convert(arabic)
        self.assertEqual(roman, converted)

    def test_3_to_III_roman(self):
        arabic = 3
        roman = 'III'
        converted = self.instance.convert(arabic)
        self.assertEqual(roman, converted)

    def test_4_to_IV_roman(self):
        arabic = 4
        roman = 'IV'
        converted = self.instance.convert(arabic)
        self.assertEqual(roman, converted)

    def test_6_to_VI_roman(self):
        arabic = 6
        roman = 'VI'
        converted = self.instance.convert(arabic)
        self.assertEqual(roman, converted)

    def test_7_to_VII_roman(self):
        arabic = 7
        roman = 'VII'
        converted = self.instance.convert(arabic)
        self.assertEqual(roman, converted)

    def test_8_to_VIII_roman(self):
        arabic = 8
        roman = 'VIII'
        converted = self.instance.convert(arabic)
        self.assertEqual(roman, converted)

    def test_9_to_IX_roman(self):
        arabic = 9
        roman = 'IX'
        converted = self.instance.convert(arabic)
        self.assertEqual(roman, converted)

    def test_5_to_V_roman(self):
        arabic = 5
        roman = 'V'
        converted = self.instance.convert(arabic)
        self.assertEqual(roman, converted)

    def test_10_to_X_roman(self):
        arabic = 10
        roman = 'X'
        converted = self.instance.convert(arabic)
        self.assertEqual(roman, converted)

    def test_50_to_L_roman(self):
        arabic = 50
        roman = 'L'
        converted = self.instance.convert(arabic)
        self.assertEqual(roman, converted)

    def test_100_to_C_roman(self):
        arabic = 100
        roman = 'C'
        converted = self.instance.convert(arabic)
        self.assertEqual(roman, converted)

    def test_500_to_D_roman(self):
        arabic = 500
        roman = 'D'
        converted = self.instance.convert(arabic)
        self.assertEqual(roman, converted)

    def test_1000_to_M_roman(self):
        arabic = 1000
        roman = 'M'
        converted = self.instance.convert(arabic)
        self.assertEqual(roman, converted)
