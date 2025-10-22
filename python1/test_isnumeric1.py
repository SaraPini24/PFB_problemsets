import pytest

from testing_problemset3 import isnumeric


def test_number_literal_returns_true():
    """Confirm the numeric literal 1.3 returns True."""
    assert isnumeric(1.3) is True


def test_string_decimal_returns_true():
    """Confirm the string '1.3' returns True."""
    assert isnumeric('1.3') is True


def test_string_scientific_returns_true():
    """Confirm the string '1e-6' returns True."""
    assert isnumeric('1e-6') is True


def test_string_negative_decimal_returns_true():
    """Confirm the string '-0.0001' returns True."""
    assert isnumeric('-0.0001') is True


def test_string_not_a_number_returns_false():
    """Confirm the string 'not-a-number' returns False."""
    assert isnumeric('not-a-number') is False
