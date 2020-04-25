from math import sin, pi

from algorithm import Algorithm


def reconstruction_switcher(reconstruction_code):
    switcher = {
        'r1': r1,
        'r2': r2,
        'r3': r3
    }
    return switcher.get(reconstruction_code.lower(), r1)


def _decorator(func):
    def function_wrapper(alg1, alg2, merge):
        assert isinstance(alg1, Algorithm)
        if alg2 is not None and merge is not None:
            assert isinstance(alg2, Algorithm)
            vector_x, vector_y = merge(alg1, alg2)
        else:
            vector_x, vector_y = alg1.perform_algorithm()

        return func(vector_x, vector_y)

    return function_wrapper


@_decorator
def r1(vector_x, vector_y):
    new_x, new_y = [], []
    for i, (x, y) in enumerate(zip(vector_x, vector_y)):
        new_x.append(x)
        new_y.append(y)
        if i < len(vector_x) - 1:
            new_x.append(vector_x[i + 1])
            new_y.append(y)
    return new_x, new_y


@_decorator
def r2(vector_x, vector_y):
    new_x, new_y = [], []
    for i, (x, y) in enumerate(zip(vector_x, vector_y)):
        new_x.append(x)
        new_y.append(y)
        if i < len(vector_x) - 1:
            new_x.append((x + vector_x[i + 1]) / 2)
            new_y.append((y + vector_y[i + 1]) / 2)
    return new_x, new_y


@_decorator
def r3(vector_x, vector_y):
    def sinc(x):
        if x != 0:
            return sin(pi * x) / (pi * x)
        else:
            return 1

    new_x, new_y = [], []
    for i, (x, y) in enumerate(zip(vector_x, vector_y)):
        new_x.append(x)
        new_y.append(y)
        if i < len(vector_x) - 1:
            middle_x = (x + vector_x[i + 1]) / 2
            middle_y = (y + vector_y[i + 1]) / 2
            new_x.append(middle_x)
            new_y.append(middle_y * sinc(x / (vector_x[i + 1] - x) - i))
    return new_x, new_y
