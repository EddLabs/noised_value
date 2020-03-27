from unittest import TestCase

from noised_value import NoisedValue
from test.base_test_cases import NoisedValueBaseTestCase


class TestNoisedValueRightDivisionWithPositiveConstant(
    TestCase, NoisedValueBaseTestCase
):
    v = NoisedValue(val=1.5, var=0.5) / 1.12
    expected_val = 1.339285
    expected_var = 0.3986
    expected_err = 0.631345
    expected_relative_err = 0.4714


class TestNoisedValueRightDivisionWithNegativeConstant(
    TestCase, NoisedValueBaseTestCase
):
    v = NoisedValue(val=1.5, var=0.5) / (-1.12)
    expected_val = -1.339285
    expected_var = 0.3986
    expected_err = 0.631345
    expected_relative_err = 0.4714


class TestNoisedValueLeftDivisionWithPositiveConstant(
    TestCase, NoisedValueBaseTestCase
):
    v = 1.12 / NoisedValue(val=1.5, var=0.5)
    expected_val = 0.746666
    expected_var = 0.12389
    expected_err = 0.35198
    expected_relative_err = 0.4714


class TestNoisedValueLeftDivisionWithNegativeConstant(
    TestCase, NoisedValueBaseTestCase
):
    v = -1.12 / NoisedValue(val=1.5, var=0.5)
    expected_val = -0.746666
    expected_var = 0.12389
    expected_err = 0.35198
    expected_relative_err = 0.4714


class TestNoisedValueDivisionWithOtherPositiveNoisedValue(
    TestCase, NoisedValueBaseTestCase
):
    v = NoisedValue(val=1.5, var=0.5) / NoisedValue(val=1.12, var=0.2)
    expected_val = 1.339285
    expected_var = 0.68458
    expected_err = 0.82739
    expected_relative_err = 0.617787
