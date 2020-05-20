from math import sin, pi

from scipy import signal

from convolutions.window import window_switcher
from core.merging import perform_merge
from core.utils import extend, multiply_vectors


def _decorator(func):
    def function_wrapper(M, fo, fs, filter_pos, window, alg1, alg2, merge):
        analog_x, analog_y = perform_merge(alg1, alg2, merge)
        vector_y, vector_h = func(M, fo, fs, analog_y, filter_pos, window)
        return extend(analog_x, len(vector_y)), vector_y, vector_h

    return function_wrapper


# funkcja oznaczona w opisie jako 4
def filter_bottom_rect_sinc(n, M, K):
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


@_decorator
def filter_response(M, fo, fs, vector_y, filter_pos="f0", window=None):
    #  vector_h = [filter_bottom_rect_sinc(n, M, K) for n in range(M)]
    vector_h = signal.firwin(M, fo, fs=fs).tolist()
    if window is not None:
        vector_h = multiply_vectors(
            vector_h,
            [window_switcher(window)(n, M) for n in range(M)]
        )
    if filter_pos == 'f2':
        vector_h = multiply_vectors(
            vector_h,
            [pow(-1, n) for n in range(M)]
        )
    return signal.upfirdn(vector_h, vector_y).tolist(), vector_h
