from unittest import TestCase

from noised_value import NoisedValue
from test.base_test_cases import NoisedValueBaseTestCase


class TestNoisedValueRightMultiplicationWithPositiveConstant(
    TestCase, NoisedValueBaseTestCase
):
    v = NoisedValue(val=1.5, var=0.5) * 1.12
    expected_val = 1.68
    expected_var = 0.6272
    expected_err = 0.79196
    expected_relative_err = 0.4714


class TestNoisedValueRightMultiplicationWithNegativeConstant(
    TestCase, NoisedValueBaseTestCase
):
    v = NoisedValue(val=1.5, var=0.5) * (-1.12)
    expected_val = -1.68
    expected_var = 0.6272
    expected_err = 0.79196
    expected_relative_err = 0.4714


class TestNoisedValueLeftMultiplicationWithPositiveConstant(
    TestCase, NoisedValueBaseTestCase
):
    v = 1.12 * NoisedValue(val=1.5, var=0.5)
    expected_val = 1.68
    expected_var = 0.6272
    expected_err = 0.79196
    expected_relative_err = 0.4714


class TestNoisedValueLeftMultiplicationWithNegativeConstant(
    TestCase, NoisedValueBaseTestCase
):
    v = -1.12 * NoisedValue(val=1.5, var=0.5)
    expected_val = -1.68
    expected_var = 0.6272
    expected_err = 0.79196
    expected_relative_err = 0.4714


class TestNoisedValueMultiplicationWithOtherPositiveNoisedValue(
    TestCase, NoisedValueBaseTestCase
):
    v = NoisedValue(val=1.5, var=0.5) * NoisedValue(val=2.3, var=2.75)
    expected_val = 3.45
    expected_var = 8.8325
    expected_err = 2.97195
    expected_relative_err = 0.861435


class TestNoisedValueMultiplicationWithOtherNegativeNoisedValue(
    TestCase, NoisedValueBaseTestCase
):
    v = NoisedValue(val=1.5, var=0.5) * NoisedValue(val=-2.3, var=2.75)
    expected_val = -3.45
    expected_var = 8.8325
    expected_err = 2.97195
    expected_relative_err = 0.861435
