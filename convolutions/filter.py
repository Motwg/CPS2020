from math import sin, pi

from convolutions.convolution import convolution
from core.merging import perform_merge


def _decorator(func):
    def function_wrapper(M, K, filter_pos, window, alg1, alg2, merge):
        _, analog_y = perform_merge(alg1, alg2, merge)
        vector_y, vector_h = func(M, K, analog_y, filter_pos, window)
        return list(range(len(vector_y))), vector_y, vector_h

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


# todo w komentarzach wypisalem mozliwe kombinacje, jednak zadna nie wydaje mi sie poprawna
@_decorator
def filter_response(M, K, vector_y, filter_pos="f0", window=None):
    vector_h = [filter_bottom_rect_sinc(n, M, K) for n in range(M)]
    if window is not None:
        # splot funkcji okna sinc
        '''
        vector_h = convolution(
            [window_switcher(window)(n, M) for n in range(M)],
            vector_h
        )'''
        # funkcja okna(sinc)
        # vector_h = [window_switcher(window)(n, M) for n in vector_h]
        # funkcja okna * sinc
        '''        
        vector_h = multiply_vectors(
            vector_h,
            [window_switcher(window)(n, M) for n in range(M)]
        ) '''
    if filter_pos == 'f2':
        # to w zasadzie "zeruje" odpowiedz, nie wiem czy tak powinno byc
        vector_h = multiply_vectors(
            vector_h,
            [pow(-1, n) for n in range(M)]
        )
    # vector_h = vector_h + [0] * (len(vector_y) - len(vector_h))
    filtered_vector_y = convolution(vector_h, vector_y, K)
    # return convolution(filtered_vector_y, vector_y), vector_h
    # return add_vectors(filtered_vector_y, vector_y), vector_h
    return filtered_vector_y + vector_y[len(filtered_vector_y):], vector_h


def multiply_vectors(v1, v2):
    if len(v2) > len(v1):
        v1, v2 = v2, v1
    return [x * y for x, y in zip(v1, v2)] + v1[len(v2):]


def add_vectors(v1, v2):
    if len(v2) > len(v1):
        v1, v2 = v2, v1
    return [x + y for x, y in zip(v1, v2)] + v1[len(v2):]
