from unittest import TestCase

from noised_value.noised_value import NoisedValue, mean
from test.base_test_cases import NoisedValueBaseTestCase


class TestNoisedValueSumOfOneValue(TestCase, NoisedValueBaseTestCase):
    v = sum([NoisedValue(val=1.5, err=0.5)])
    expected_val = 1.5
    expected_var = 0.25
    expected_err = 0.5
    expected_relative_err = 0.33333


class TestNoisedValueSumOfTwoValues(TestCase, NoisedValueBaseTestCase):
    v = sum([NoisedValue(val=1.5, err=0.5), NoisedValue(val=0.9, err=0.1)])
    expected_val = 2.4
    expected_var = 0.26
    expected_err = 0.5099
    expected_relative_err = 0.21246


class TestNoisedValueSumOfThreeValues(TestCase, NoisedValueBaseTestCase):
    v = sum(
        [
            NoisedValue(val=1.5, err=0.5),
            NoisedValue(val=0.9, err=0.1),
            NoisedValue(val=1.2, err=0.3),
        ]
    )
    expected_val = 3.6
    expected_var = 0.35
    expected_err = 0.59161
    expected_relative_err = 0.164335


class TestNoisedValueAverageOfOneValue(TestCase, NoisedValueBaseTestCase):
    v = mean([NoisedValue(val=1.5, err=0.5)])
    expected_val = 1.5
    expected_var = 0.25
    expected_err = 0.5
    expected_relative_err = 0.33333


class TestNoisedValueAverageOfTwoValues(TestCase, NoisedValueBaseTestCase):
    v = mean([NoisedValue(val=1.5, err=0.5), NoisedValue(val=0.9, err=0.1)])
    expected_val = 1.2
    expected_var = 0.065
    expected_err = 0.25495
    expected_relative_err = 0.21246


class TestNoisedValueAverageOfThreeValues(TestCase, NoisedValueBaseTestCase):
    v = mean(
        [
            NoisedValue(val=1.5, err=0.5),
            NoisedValue(val=0.9, err=0.1),
            NoisedValue(val=1.2, err=0.3),
        ]
    )
    expected_val = 1.2
    expected_var = 0.03889
    expected_err = 0.1972
    expected_relative_err = 0.164335
