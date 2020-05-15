from math import sin, pi, cos

from convolutions.convolution import convolution
from core.merging import perform_merge


def _decorator(func):
    def function_wrapper(M, K, alg1, alg2, merge):
        _, analog_y = perform_merge(alg1, alg2, merge)
        vector_y, vector_h = func(M, K, analog_y)
        return list(range(len(vector_y))), vector_y, vector_h

    return function_wrapper


# funkcja oznaczona w opisie jako 4
def filter_bottom_sinc(n, M, K):
    if n != (M - 1) / 2:
        return sin(((2 * pi) * (n - (M - 1) / 2)) / K) / (pi * (n - (M - 1) / 2))
    else:
        return 2.0 / K


# funkcja oznaczona w opisie jako (nic?)
def filter_bottom_rect(n, M, K):
    if n != 0:
        return sin((2 * pi * n) / K) / (pi * n)
    else:
        return 2.0 / K


# okno Hanninga wzór 6
def hanning_window(n, M):
    return 0.5 - 0.5 * cos((2 * pi * n) / M)


# todo nie dziala raczej tak jak nalezy,
#  trzeba poprawic uzywajac powyzszych funkcji i splotu
@_decorator
def filter_response(M, K, vector_y):
    print(vector_y)
    vector_h = [filter_bottom_sinc(n, M, K) for n in range(M)]
    print(vector_h)
    filtered_vector_y = convolution(vector_h, vector_y, K)
    return filtered_vector_y + vector_y[len(filtered_vector_y):], vector_h
