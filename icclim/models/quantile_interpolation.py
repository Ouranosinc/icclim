from enum import Enum


class QuantileInterpolation(Enum):
    # TODO To remove once numpy and xclim support other methods (see https://github.com/numpy/numpy/pull/19857)
    LINEAR = ("linear", 1, 1)
    MEDIAN_UNBIASED = ("hyndman_fan", 1.0 / 3, 1.0 / 3)

    def __init__(self, alias, alpha, beta):
        self.alias = alias
        self.alpha = alpha
        self.beta = beta


def get_interpolation(s: str):
    for interpolation in QuantileInterpolation:
        if interpolation.value.upper() == s.upper():
            return interpolation
    valid_values = list(map(lambda x: x.value, QuantileInterpolation))
    raise NotImplementedError(
        f"Interpolation must be one of the following: {valid_values}"
    )
