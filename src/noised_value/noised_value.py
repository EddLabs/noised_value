import math

PLUS_MINUS = "\u00B1"


class NoisedValue:

    def __init__(self, val, var=None, err=None):
        self.val = val
        self.__set_initial_errors(var, err)

    @property
    def var(self):
        if self.__var is None:
            self.__var = self.err ** 2
        return self.__var

    @property
    def err(self):
        if self.__err is None:
            self.__err = math.sqrt(self.var)
        return self.__err

    @property
    def relative_err(self):
        if self.__relative_err is None:
            self.__relative_err = self.__calc_relative_error()
        return self.__relative_err

    def n_sigma(self, other):
        return math.fabs(self.val - other.val) / math.sqrt(self.var + other.var)

    def __neg__(self):
        return NoisedValue(val=-self.val, var=self.var)

    def __add__(self, other):
        if isinstance(other, NoisedValue):
            return NoisedValue(val=self.val + other.val, var=self.var + other.var)
        return NoisedValue(val=self.val + other, var=self.var)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -(self + (-other))

    def __mul__(self, other):
        if isinstance(other, NoisedValue):
            return NoisedValue(val=self.val * other.val, var=self.var * other.val ** 2 + other.var * self.val ** 2)
        return NoisedValue(val=self.val * other, var=self.var * other ** 2)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, NoisedValue):
            new_var = (self.var * other.val ** 2 + other.var * self.val ** 2) / (other.val ** 4)
            return NoisedValue(val=self.val / other.val, var=new_var)
        return NoisedValue(val=self.val / other, var=self.var / (other ** 2))

    def __rtruediv__(self, other):
        return NoisedValue(val=other) / self

    def __pow__(self, power):
        if power == 0:
            return NoisedValue(val=1)
        new_val = self.val ** power
        new_var = (power ** 2) * (self.val ** (2 * power - 2)) * self.var
        return NoisedValue(val=new_val, var=new_var)

    def __repr__(self):
        return f"{self.val} {PLUS_MINUS} {self.err} ({self.relative_err * 100 :.3f}% error)"

    def __calc_relative_error(self):
        if self.val == 0:
            return 0
        return self.err / math.fabs(self.val)

    def __set_initial_errors(self, var, err):
        if var is None and err is None:
            self.__var = self.__err = self.__relative_err = 0
            return
        if var is not None:
            if var < 0:
                raise ValueError(f"Variance must be non-negative, got {var}")
            if err is not None:
                raise ValueError("Cannot create a LabValue with both variance and error")
        if err is not None and err < 0:
            raise ValueError(f"Error must be non-negative, got {err}")
        self.__var = var
        self.__err = err
        self.__relative_err = None


def zero():
    return NoisedValue(0)


def one():
    return NoisedValue(1)


def mean(lst):
    return sum(lst) / len(lst)
