from unittest import TestCase

from noised_value.noised_value import zero, one
from test.base_test_cases import NoisedValueBaseTestCase


class TestNoisedValueZero(TestCase, NoisedValueBaseTestCase):
    v = zero()
    expected_val = 0
    expected_var = 0
    expected_err = 0
    expected_relative_err = None


class TestNoisedValueOne(TestCase, NoisedValueBaseTestCase):
    v = one()
    expected_val = 1
    expected_var = 0
    expected_err = 0
    expected_relative_err = 0
