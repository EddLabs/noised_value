from unittest import TestCase

from noised_value import NoisedValue
from test.base_test_cases import NoisedValueBaseTestCase


class TestNoisedValueInteger1Power(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, err=0.5) ** 1
    expected_val = 1.5
    expected_var = 0.25
    expected_err = 0.5
    expected_relative_err = 0.33333


class TestNoisedValueInteger2Power(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, err=0.5) ** 2
    expected_val = 2.25
    expected_var = 2.25
    expected_err = 1.5
    expected_relative_err = 0.666666


class TestNoisedValueInteger3Power(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, err=0.5) ** 3
    expected_val = 3.375
    expected_var = 11.390625
    expected_err = 3.375
    expected_relative_err = 1


class TestNoisedValueInteger0Power(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, err=0.5) ** 0
    expected_val = 1
    expected_var = 0
    expected_err = 0
    expected_relative_err = 0


class TestNoisedValueIntegerNegativePower(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, err=0.5) ** -1
    expected_val = 0.666666
    expected_var = 0.049382
    expected_err = 0.222222
    expected_relative_err = 0.333333
