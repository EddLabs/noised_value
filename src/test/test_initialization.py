from unittest import TestCase

from noised_value import NoisedValue
from test.base_test_cases import NoisedValueBaseTestCase


class TestNoisedValueInitializationWithoutVarianceOrError(
    TestCase, NoisedValueBaseTestCase
):
    v = NoisedValue(val=1.5)
    expected_val = 1.5
    expected_var = 0
    expected_err = 0
    expected_relative_err = 0


class TestNoisedValueInitializationWithVariance(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, err=0.5)
    expected_val = 1.5
    expected_var = 0.25
    expected_err = 0.5
    expected_relative_err = 0.33333


class TestNoisedValueInitializationWithError(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, err=0.5)
    expected_val = 1.5
    expected_var = 0.25
    expected_err = 0.5
    expected_relative_err = 0.33333


class TestNoisedValueInitializationWithValueZero(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=0, err=0.5)
    expected_val = 0
    expected_var = 0.25
    expected_err = 0.5
    expected_relative_err = None


class TestNoisedValueInitializationRaiseError(TestCase):
    def test_init_with_both_variance_and_error_raises_value_error(self):
        self.assertRaises(ValueError, NoisedValue, val=1.5, var=0.25, err=0.5)

    def test_init_with_negative_variance_raises_value_error(self):
        self.assertRaises(ValueError, NoisedValue, val=1.5, var=-0.25)

    def test_init_with_negative_error_raises_value_error(self):
        self.assertRaises(ValueError, NoisedValue, val=1.5, err=-0.5)
