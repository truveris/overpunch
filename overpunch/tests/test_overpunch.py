# Copyright 2015-2017, Truveris Inc. All Rights Reserved.

import sys
import random
import unittest
from decimal import Decimal, ROUND_FLOOR

import overpunch


class TestCase(unittest.TestCase):

    """
    Test cases for overpunched extraction and formatting.
    """

    def test_extract_no_decimal_positive(self):
        d = Decimal("1234.50")
        self.assertEquals(overpunch.extract("12345{"), d)

    def test_extract_no_decimal_negative(self):
        d = Decimal("-1234.50")
        self.assertEquals(overpunch.extract("12345}"), d)

    def test_extract_4_decimal_negative(self):
        d = Decimal("-12.3450")
        self.assertEquals(overpunch.extract("12345}", decimals=4), d)

    def test_extract_0_decimal_negative(self):
        d = Decimal("-123450")
        self.assertEquals(overpunch.extract("12345}", decimals=0), d)

    def test_format_no_decimal_positive(self):
        d = Decimal("1234.50")
        self.assertEquals("12345{", overpunch.format(d))

    def test_format_no_decimal_negative(self):
        d = Decimal("-1234.50")
        self.assertEquals("12345}", overpunch.format(d))

    def test_format_4_decimal_negative(self):
        d = Decimal("-12.3450")
        self.assertEquals("12345}", overpunch.format(d, decimals=4))

    def test_format_0_decimal_negative(self):
        d = Decimal("-123450")
        self.assertEquals("12345}", overpunch.format(d, decimals=0))

    def test_format_2_decimal_round_default(self):
        d = Decimal("12.3450")
        self.assertEquals("123E", overpunch.format(d, decimals=2))

    def test_format_2_decimal_negative_round_default(self):
        d = Decimal("-12.3450")
        self.assertEquals("123N", overpunch.format(d, decimals=2))

    def test_format_2_decimal_round_custom(self):
        d = Decimal("12.3450")
        self.assertEquals("123D", overpunch.format(d, decimals=2,
                                                   rounding=ROUND_FLOOR))

    def test_format_2_decimal_negative_round_custom(self):
        d = Decimal("-12.3450")
        self.assertEquals("123N", overpunch.format(d, decimals=2,
                                                   rounding=ROUND_FLOOR))

    def test_nan_raises(self):
        d = Decimal("NaN")
        with self.assertRaises(ValueError):
            overpunch.format(d)

    def test_format_integer(self):
        d = 150
        self.assertEquals("15{", overpunch.format(d, decimals=0))

    def test_random(self):
        for i in range(1000):
            d = Decimal(random.randint(0, sys.maxsize)) / 100
            if random.random() > 0.5:
                d = -d

            self.assertEquals(overpunch.extract(overpunch.format(d)), d)
