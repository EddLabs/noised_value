import math

PLUS_MINUS = "\u00B1"


class LabValue:

    def __init__(self, val, var=None, err=None):
        self.val = val
        self.__set_initial_errors(var, err)

    @property
    def var(self):
        if self.__var is None:
            self.__var = self.__err ** 2
        return self.__var

    @property
    def err(self):
        if self.__err is None:
            self.__err = math.sqrt(self.__var)
        return self.__err

    def __neg__(self):
        return LabValue(val=-self.val, var=self.var)

    def __add__(self, other):
        if isinstance(other, LabValue):
            return LabValue(val=self.val + other.val, var=self.var + other.var)
        return LabValue(val=self.val + other, var=self.var)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return -(self + (-other))

    def __mul__(self, other):
        if isinstance(other, LabValue):
            return LabValue(val=self.val * other.val, var=self.var * other.val ** 2 + other.var * self.val ** 2)
        return LabValue(val=self.val * other, err=math.fabs(other) * self.err)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, LabValue):
            new_var = (self.var * other.val ** 2 + other.var * self.val ** 2) / (other.val ** 4)
            return LabValue(val=self.val / other.val, var=new_var)
        return LabValue(val=self.val / other, err=self.err / math.fabs(other))

    def __rtruediv__(self, other):
        return LabValue(val=other) / self

    def __pow__(self, power):
        return LabValue(val=self.val ** power, err=power * self.err * self.val ** (power - 1))

    def __set_initial_errors(self, var, err):
        if var is None and err is None:
            self.__var = self.__err = 0
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

    def __repr__(self):
        return f"{self.val} {PLUS_MINUS} {self.err}"
