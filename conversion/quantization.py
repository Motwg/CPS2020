from math import fabs

from numpy import arange

from algorithm import Algorithm


def quantization_switcher(quantization_code):
    switcher = {
        'q2': q2
    }
    return switcher.get(quantization_code.lower(), q2)


def quantization(vector_y, quantization_steps):
    max_y, min_y = max(vector_y), min(vector_y)
    diff = (max_y - min_y) / quantization_steps
    return list(arange(min_y, max_y + diff, diff))


def _decorator(func):
    def function_wrapper(steps, alg1, alg2, merge):
        assert isinstance(alg1, Algorithm)
        if alg2 is not None and merge is not None:
            assert isinstance(alg2, Algorithm)
            vector_x, vector_y = merge(alg1, alg2)
        else:
            vector_x, vector_y = alg1.perform_algorithm()
        return vector_x, func(vector_y, quantization(vector_y, steps))

    return function_wrapper


# Kwantyzacja z zaokrągleniem
@_decorator
def q2(vector_y, values):
    def approximate(y, quantization_values):
        assert isinstance(quantization_values, list)
        nearest, dist = quantization_values[0], fabs(y - quantization_values[0])
        for value in quantization_values:
            new_dist = fabs(y - value)
            if new_dist < dist:
                nearest, dist = value, new_dist
        return nearest
    return [approximate(y, values) for y in vector_y]
