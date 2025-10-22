import pytest

from testing_problemsetAI import isnumeric


def test_number_literal_returns_true():
    assert isnumeric(1.3) is True


def test_string_decimal_returns_true():
    assert isnumeric('1.3') is True


def test_string_scientific_returns_true():
    assert isnumeric('1e-6') is True


def test_string_negative_decimal_returns_true():
    assert isnumeric('-0.0001') is True


def test_string_not_a_number_returns_false():
    assert isnumeric('not-a-number') is False


def test_none_returns_false():
    assert isnumeric(None) is False


def test_boolean_values():
    # True and False are instances of int subclasses in Python; float(True) -> 1.0
    # The implementation uses float() so booleans are considered numeric here.
    assert isnumeric(True) is True
    assert isnumeric(False) is True

def test_complex_input_returns_false():
    """Complex numbers cannot be converted to float, so should return False."""
    assert isnumeric(1+5j) is False
