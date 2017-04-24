# Copyright 2015-2017, Truveris Inc. All Rights Reserved.

"""
Extract and generate overpunch formatted numbers.
"""

from decimal import Decimal, ROUND_HALF_UP


__copyright__ = "(c) 2015 Truveris"
__version__ = "1.1"


EXTRACT_REF = {
    "0": ("+", "0"),
    "1": ("+", "1"),
    "2": ("+", "2"),
    "3": ("+", "3"),
    "4": ("+", "4"),
    "5": ("+", "5"),
    "6": ("+", "6"),
    "7": ("+", "7"),
    "8": ("+", "8"),
    "9": ("+", "9"),
    "{": ("+", "0"),
    "A": ("+", "1"),
    "B": ("+", "2"),
    "C": ("+", "3"),
    "D": ("+", "4"),
    "E": ("+", "5"),
    "F": ("+", "6"),
    "G": ("+", "7"),
    "H": ("+", "8"),
    "I": ("+", "9"),
    "}": ("-", "0"),
    "J": ("-", "1"),
    "K": ("-", "2"),
    "L": ("-", "3"),
    "M": ("-", "4"),
    "N": ("-", "5"),
    "O": ("-", "6"),
    "P": ("-", "7"),
    "Q": ("-", "8"),
    "R": ("-", "9"),
}


def extract(raw, decimals=2):
    """Extract a number in the overpunch format to a Decimal object.

    :param raw: The formatted value.
    :param decimals: The implied decimal precision of this number (default: 2).

    """

    length = len(raw)
    last_char = raw[length - 1]
    (sign, cent) = EXTRACT_REF[last_char]

    if not decimals:
        core = raw[:-1]
    else:
        core = raw[:length-decimals] + "." + raw[length-decimals:-1]

    return Decimal(sign + core + cent)


FORMAT_REF = {
    ("+", "0"): "{",
    ("+", "1"): "A",
    ("+", "2"): "B",
    ("+", "3"): "C",
    ("+", "4"): "D",
    ("+", "5"): "E",
    ("+", "6"): "F",
    ("+", "7"): "G",
    ("+", "8"): "H",
    ("+", "9"): "I",
    ("-", "0"): "}",
    ("-", "1"): "J",
    ("-", "2"): "K",
    ("-", "3"): "L",
    ("-", "4"): "M",
    ("-", "5"): "N",
    ("-", "6"): "O",
    ("-", "7"): "P",
    ("-", "8"): "Q",
    ("-", "9"): "R",
}


def format(val, decimals=2, rounding=ROUND_HALF_UP):
    """Convert a number to an overpunch-formatted string.

    :param val: The number to format.
    :param decimals: How many decimals are implied in the formatted value
        (default: 2).
    :param rounding: When rounding a value during quantization, how that value
        is to be rounded. Appropriate values are the rounding constants from
        the ``decimal`` library (default: ROUND_HALF_UP).

    """

    if not isinstance(val, Decimal):
        val = Decimal(str(val))

    if val.is_nan():
        raise ValueError("{} is NaN".format(val))

    # force the correct number of decimal digits
    quantize_str = "1"
    if decimals:
        quantize_str = quantize_str + "." + ("0" * decimals)

    val = val.quantize(Decimal(quantize_str), rounding)

    # we'll need this to figure out how to format the last character
    if val.is_signed():
        sign = "-"
    else:
        sign = "+"

    # get rid of the sign
    val = abs(val)

    # turn into a string
    val = str(val)

    # remove the "."
    val = val.replace(".", "")

    # split, replace the last digit with the right format character, join
    parts = list(val)
    parts[-1] = FORMAT_REF[(sign, parts[-1])]

    return "".join(parts)
