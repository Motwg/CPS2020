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
        alg4 = None
        if alg2 is not None:
            assert isinstance(alg2, Algorithm)
            alg4 = alg2.__copy__()
        alg3 = alg1.__copy__()
        return func(alg3, alg4, merge)

    return function_wrapper

@_decorator
def r1(alg1, alg2, merge):
    if merge is None or alg2 is None:
        vector_x, vector_y = alg1.perform_algorithm()
    else:
        vector_x, vector_y = merge(alg1, alg2)

    new_x, new_y = [], []
    for i, (x, y) in enumerate(zip(vector_x, vector_y)):
        new_x.append(x)
        new_y.append(y)
        if i < len(vector_x) - 1:
            new_x.append(vector_x[i + 1])
            new_y.append(y)
    return new_x, new_y

@_decorator
def r2(alg1, alg2, merge):
    if merge is None or alg2 is None:
        vector_x, vector_y = alg1.perform_algorithm()
    else:
        vector_x, vector_y = merge(alg1, alg2)

    new_x, new_y = [], []
    for i, (x, y) in enumerate(zip(vector_x, vector_y)):
        new_x.append(x)
        new_y.append(y)
        if i < len(vector_x) - 1:
            new_x.append((x + vector_x[i + 1]) / 2)
            new_y.append((y + vector_y[i + 1]) / 2)
    return new_x, new_y

@_decorator
def r3(alg1, alg2, merge):
    def sinc(x):
        if x != 0:
            return sin(pi * x) / (pi * x)
        else:
            return 1

    if merge is None or alg2 is None:
        vector_x, vector_y = alg1.perform_algorithm()
    else:
        vector_x, vector_y = merge(alg1, alg2)

    new_x, new_y = [], []
    for i, (x, y) in enumerate(zip(vector_x, vector_y)):
        new_x.append(x)
        new_y.append(y)
        if i < len(vector_x) - 1:
            middle_x = (x + vector_x[i + 1]) / 2
            middle_y = (y + vector_y[i + 1]) / 2
            new_x.append(middle_x)
            new_y.append(middle_y * sinc(x / alg1.kwargs['f'] - i))
    return new_x, new_y
