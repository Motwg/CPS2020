from itertools import starmap
from math import fabs, log10

from core.algorithm import Algorithm


def similarity_switcher(similarity_code):
    switcher = {
        'c1': c1,
        'c2': c2,
        'c4': c4
    }
    return switcher.get(similarity_code.lower(), c1)


def _decorator(func):
    def function_wrapper(vector_x, vector_y, alg1, alg2, merge):
        assert isinstance(alg1, Algorithm)
        alg3, alg4 = alg1.__copy__(), None
        # change of frequency
        alg3.kwargs['f'] = fabs(vector_x[0] - vector_x[1])
        if alg2 is not None and merge is not None:
            assert isinstance(alg2, Algorithm)
            alg4 = alg2.__copy__()
            _, analog_y = merge(alg3, alg4)
        else:
            _, analog_y = alg3.perform_algorithm()
        return func(analog_y[:len(vector_y)], vector_y)

    return function_wrapper


def squared_error(v1, v2):
    diff = (v1 - v2)
    return diff * diff


# Błąd średniokwadratowy (MSE)
@_decorator
def c1(analog_y, vector_y):
    return sum(starmap(squared_error, zip(analog_y, vector_y))) / len(analog_y)


# Stosunek sygnał - szum (SNR)
@_decorator
def c2(analog_y, vector_y):
    divisor = sum(starmap(squared_error, zip(analog_y, vector_y)))
    if divisor != 0:
        return 10 * log10(sum(map(lambda v: v * v, analog_y)) / divisor)
    else:
        return 0


# Maksymalna różnica (MD)
@_decorator
def c4(analog_y, vector_y):
    return max(list(starmap(lambda v1, v2: fabs(v1 - v2), zip(analog_y, vector_y))))
