from collections import deque
from math import sin, pi

from core.merging import perform_merge


def reconstruction_switcher(reconstruction_code):
    switcher = {
        'r1': r1,
        'r2': r2,
        'r3': r3
    }
    return switcher.get(reconstruction_code.lower(), r1)


def _decorator(func):
    def function_wrapper(vector_x, vector_y, alg1, alg2, merge):
        analog_x, analog_y = perform_merge(alg1, alg2, merge)
        return func(vector_x, vector_y, analog_x)

    return function_wrapper


@_decorator
def r1(vector_x, vector_y, analog_x):
    new_y = []
    queue = deque(zip(vector_x, vector_y))
    (x, y) = queue.pop()
    analog_x.reverse()
    for ax in analog_x:
        while round(ax, 5) < round(x, 5):
            (x, y) = queue.pop()
        else:
            new_y.append(y)
    return analog_x, new_y


@_decorator
def r2(vector_x, vector_y, analog_x):
    new_y = []
    queue = deque(zip(vector_x, vector_y))
    an_queue = deque(analog_x)
    ax = an_queue.popleft()
    (x, y) = queue.popleft()
    (next_x, next_y) = queue.popleft()

    try:
        while round(x, 5) <= round(ax, 5):
            while round(ax, 5) < round(next_x, 5):
                new_y.append(y + (next_y - y) * (ax - x) / (next_x - x))
                ax = an_queue.popleft()
            x, y = next_x, next_y
            (next_x, next_y) = queue.popleft()
    except IndexError:
        new_y.append(vector_y[-1])
        return analog_x[:len(new_y)], new_y


@_decorator
def r3(vector_x, vector_y, analog_x):
    def sinc(x):
        if x != 0:
            return sin(pi * x) / (pi * x)
        else:
            return 1

    new_y = []
    T = vector_x[1] - vector_x[0]
    for an in analog_x:
        new_y.append(sum([y * sinc(an / T - i) for i, y in enumerate(vector_y)]))
    return analog_x, new_y
