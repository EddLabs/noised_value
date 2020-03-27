import numpy as np
from unittest import TestCase

from noised_value import NoisedValue
from test.base_test_cases import NoisedValueBaseTestCase


class TestNoisedValueExponential(TestCase, NoisedValueBaseTestCase):
    v = np.exp(NoisedValue(val=1.5, err=0.5))
    expected_val = 4.48169
    expected_var = 5.02138
    expected_err = 2.24084
    expected_relative_err = 0.5


class TestNoisedValueSin(TestCase, NoisedValueBaseTestCase):
    v = np.sin(NoisedValue(val=np.pi / 6, err=0.5))
    expected_val = 0.5
    expected_var = 0.1875
    expected_err = 0.433013
    expected_relative_err = 0.866025


class TestNoisedValueCos(TestCase, NoisedValueBaseTestCase):
    v = np.cos(NoisedValue(val=np.pi / 6, err=0.5))
    expected_val = 0.866025
    expected_var = 0.0625
    expected_err = 0.25
    expected_relative_err = 0.288675
