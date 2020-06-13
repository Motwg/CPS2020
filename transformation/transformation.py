import time

import numpy as np
from pywt import dwt, idwt  # pip install PyWavelets
from scipy.fft import fft, ifft

last_db4_cD = []


def transformation_switcher(transformation_code):
    switcher = {
        'dft': (dft, idft),
        'f2': (fft2f, ifft2f),
        't3': (db4, idb4)
    }
    return switcher.get(transformation_code.lower(), 'f2')


def _decorator(func):
    def function_wrapper(vector):
        assert isinstance(vector, list)
        start = time.perf_counter()
        result = func(vector)
        stop = time.perf_counter()
        return result, stop - start

    return function_wrapper


@_decorator
def dft(vector_y):
    v_y = []
    vector_y_len = len(vector_y)
    for m in range(vector_y_len):
        value = 0
        for n in range(vector_y_len):
            value += vector_y[n] * np.exp(-2j * np.pi * m * n / vector_y_len, dtype=np.complex_)
        v_y.append(value / vector_y_len)
    return v_y


@_decorator
def idft(vector_y):
    v_y = []
    vector_y_len = len(vector_y)
    for n in range(vector_y_len):
        value = 0
        for m in range(vector_y_len):
            value += vector_y[m] * np.exp(2j * np.pi * m * n / vector_y_len, dtype=np.complex_)
        v_y.append(value)
    return v_y


@_decorator
def fft2f(vector_y):
    return list(fft(vector_y, n=len(vector_y)))


@_decorator
def ifft2f(vector_y):
    return list(ifft(vector_y))


@_decorator
def db4(vector_y):
    global last_db4_cD
    real, last_db4_cD = dwt(vector_y, 'db4')
    # list(map(lambda r, i: complex(r, i), real, imag))
    return list(real)


@_decorator
def idb4(vector_y):
    global last_db4_cD
    real = list(idwt(vector_y, last_db4_cD, 'db4'))
    return real


if __name__ == '__main__':
    vec = np.sin(2. * np.pi / 8 * np.arange(0, 8))
    dvec, t = dft(vec)
    idvec, t = idft(dvec)

    print(vec)
    print(dvec)
    print(idvec)
