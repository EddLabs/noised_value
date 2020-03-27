from unittest import TestCase

from noised_value import NoisedValue
from test.base_test_cases import NoisedValueBaseTestCase


class TestNoisedValueRightConstantAddition(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, var=0.5) + 2.2
    expected_val = 3.7
    expected_var = 0.5
    expected_err = 0.70711
    expected_relative_err = 0.19111


class TestNoisedValueLeftConstantAddition(TestCase, NoisedValueBaseTestCase):
    v = 2.2 + NoisedValue(val=1.5, var=0.5)
    expected_val = 3.7
    expected_var = 0.5
    expected_err = 0.70711
    expected_relative_err = 0.19111


class TestNoisedValueAdditionWithOtherNoisedValue(TestCase, NoisedValueBaseTestCase):
    v = NoisedValue(val=1.5, var=0.5) + NoisedValue(val=2.2, var=2.75)
    expected_val = 3.7
    expected_var = 3.25
    expected_err = 1.802775
    expected_relative_err = 0.487236
