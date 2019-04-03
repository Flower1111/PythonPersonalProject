from unittest import TestCase, main
from PythonPersonalProject.Python.models.converting_number_to_word import number_to_word


class Num2WordsRUTest(TestCase):

    def test_different_numbers(self):
        self.assertEqual(number_to_word(1), "один")
        self.assertEqual(number_to_word(12), "двенадцать")
        self.assertEqual(number_to_word(100), "сто")
        self.assertEqual(number_to_word(102), "сто два")
        self.assertEqual(number_to_word(110), "сто десять")
        self.assertEqual(number_to_word(115), "сто пятнадцать")
        self.assertEqual(number_to_word(135), "сто тридцать пять")
        self.assertEqual(number_to_word(1000), "одна тысяча")
        self.assertEqual(number_to_word(1001), "одна тысяча один")
        self.assertEqual(number_to_word(1233), "одна тысяча двести тридцать три")
        self.assertEqual(number_to_word(2010), "две тысячи десять")
        self.assertEqual(number_to_word(312244), "триста двенадцать тысяч двести сорок четыре")
        self.assertEqual(number_to_word(1000128), "один миллион сто двадцать восемь")
        self.assertEqual(number_to_word(567101011), "пятьсот шестьдесят семь миллионов сто одна тысяча одиннадцать")

    def test_negative_number(self):
        self.assertEqual(number_to_word(-1), "минус один")
        self.assertEqual(number_to_word(-121.2), "минус сто двадцать один запятая два")

    def test_floating_point(self):
        self.assertEqual(number_to_word(2.3), "два запятая три")
        self.assertEqual(number_to_word(342.36), "триста сорок два запятая тридцать шесть")

    def test_text(self):
        self.assertEqual(number_to_word('-7'), "минус семь")
        self.assertEqual(number_to_word("-208.12"), "минус двести восемь запятая двенадцать")


if __name__ == '__main__':
    main()
