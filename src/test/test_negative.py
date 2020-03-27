from unittest import TestCase

from noised_value import NoisedValue
from test.base_test_cases import NoisedValueBaseTestCase


class TestNoisedValueNegativeValue(TestCase, NoisedValueBaseTestCase):
    v = -NoisedValue(val=1.5, var=0.5)
    expected_val = -1.5
    expected_var = 0.5
    expected_err = 0.70711
    expected_relative_err = 0.4714
