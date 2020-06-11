def transformation_switcher(transformation_code):
    switcher = {
        'f2': (fft2f, ifft2f),
        't3': (db4, idb4)
    }
    return switcher.get(transformation_code.lower(), 'f2')


def fft2f():
    pass


def ifft2f():
    pass


def db4():
    pass


def idb4():
    pass
