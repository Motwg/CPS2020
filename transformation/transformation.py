import numpy as np


def transformation_switcher(transformation_code):
    switcher = {
        'dft': (dft, idft),
        'f2': (fft2f, ifft2f),
        't3': (db4, idb4)
    }
    return switcher.get(transformation_code.lower(), 'f2')


def dft(vector_y):
    v_y = []
    vector_y_len = len(vector_y)
    for m in range(vector_y_len):
        value = 0
        for n in range(vector_y_len):
            value += vector_y[n] * np.exp(-2j * np.pi * m * n / vector_y_len, dtype=np.complex_)
        v_y.append(value / vector_y_len)
    return v_y


def idft(vector_y):
    v_y = []
    vector_y_len = len(vector_y)
    for n in range(vector_y_len):
        value = 0
        for m in range(vector_y_len):
            value += vector_y[m] * np.exp(2j * np.pi * m * n / vector_y_len, dtype=np.complex_)
        v_y.append(value)
    return v_y


def fft2f():
    pass


def ifft2f():
    pass


def db4():
    pass


def idb4():
    pass


if __name__ == '__main__':
    vec = [1,0,3,4,6,0]
    dvec = dft(vec)
    idvec = idft(dvec)

    print(dvec)
    print(idvec)