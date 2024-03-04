import functions.calc as fc
import pytest


def test_negatives():
    assert fc.adivb(-10, -5) > 0, "Two negatives should return a positive."


def test_posneg():
    assert (fc.adivb(-9, 3) < 0), "One positive and one negative should return a negative."


def test_positives():
    assert fc.adivb(35, 7) > 0, "Two positives should return a positive."


def test_type():
    assert isinstance(fc.adivb(5, 10), float ), "Odd divided by Evens should return a float."


def test_float():
    assert fc.adivb(5, 2) == 2.5, "5/2 should be 2.5."


def test_rational():
    assert fc.adivb(10, 3) == pytest.approx(3.33, 0.01), "10/3 should be 3.33."


# test
# import pytest
# assert type(adivb(50,10), float), "Larger number divided by lower number should return value > 1."
# assert type(adivb(5,10), float), "Lower number divided by larger number should return value < 1."
