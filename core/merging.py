from numpy import nan

from convolutions import convolution
from core.algorithm import Algorithm


def merge_switcher(merging_code):
    switcher = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '(h * x)(n)': convolution_merge
    }
    return switcher.get(merging_code, add)


def _decorator(func):
    def function_wrapper(alg1, alg2):
        assert isinstance(alg1, Algorithm)
        assert isinstance(alg2, Algorithm)

        # takes t1, d and f parameters from first function
        for kwarg in ['t1', 'd', 'f']:
            alg2.kwargs[kwarg] = alg1.kwargs[kwarg]
        return func(alg1, alg2)

    return function_wrapper


@_decorator
def add(alg1, alg2):
    vector_x, vector_y1 = alg1.perform_algorithm()
    _, vector_y2 = alg2.perform_algorithm()
    assert len(vector_y1) == len(vector_y2)
    return vector_x, [y1 + y2 for y1, y2 in zip(vector_y1, vector_y2)]


@_decorator
def subtract(alg1, alg2):
    vector_x, vector_y1 = alg1.perform_algorithm()
    _, vector_y2 = alg2.perform_algorithm()
    assert len(vector_y1) == len(vector_y2)
    return vector_x, [y1 - y2 for y1, y2 in zip(vector_y1, vector_y2)]


@_decorator
def multiply(alg1, alg2):
    vector_x, vector_y1 = alg1.perform_algorithm()
    _, vector_y2 = alg2.perform_algorithm()
    assert len(vector_y1) == len(vector_y2)
    return vector_x, [y1 * y2 for y1, y2 in zip(vector_y1, vector_y2)]


@_decorator
def divide(alg1, alg2):
    vector_x, vector_y1 = alg1.perform_algorithm()
    _, vector_y2 = alg2.perform_algorithm()
    assert len(vector_y1) == len(vector_y2)
    vector_y = []
    for y1, y2 in zip(vector_y1, vector_y2):
        if y2 != 0:
            vector_y.append(y1 / y2)
        else:
            vector_y.append(nan)
    return vector_x, vector_y


def convolution_merge(alg1, alg2):
    assert isinstance(alg1, Algorithm)
    assert isinstance(alg2, Algorithm)
    vector_x1, vector_y1 = alg1.perform_algorithm()
    vector_x2, vector_y2 = alg2.perform_algorithm()
    vector_y = convolution.convolution(vector_y1, vector_y2)
    return [x for x in range(len(vector_y))], vector_y


def perform_merge(alg1, alg2, merge_method):
    assert isinstance(alg1, Algorithm)
    if alg2 is not None and merge_method is not None:
        assert isinstance(alg2, Algorithm)
        return merge_method(alg1, alg2)
    else:
        return alg1.perform_algorithm()
