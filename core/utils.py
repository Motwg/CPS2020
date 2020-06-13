import cmath


def multiply_vectors(v1, v2):
    if len(v2) > len(v1):
        v1, v2 = v2, v1
    return [x * y for x, y in zip(v1, v2)] + v1[len(v2):]


def add_vectors(v1, v2):
    if len(v2) > len(v1):
        v1, v2 = v2, v1
    return [x + y for x, y in zip(v1, v2)] + v1[len(v2):]


def extend(v, length):
    while len(v) < length:
        v.append(v[-1] + v[1] - v[0])
    return v


def split_complex(vector, w='W1'):
    if isinstance(vector, list) and len(vector) > 0:
        if isinstance(vector[0], complex):
            if w == 'W1':
                real, imag = [], []
                for v in vector:
                    real.append(v.real)
                    imag.append(v.imag)
                return real, imag
            else:
                mod, arg = [], []
                for v in vector:
                    pol = cmath.polar(v)
                    mod.append(pol[0])
                    arg.append(pol[1])
                return mod, arg
        else:
            return vector, [0] * len(vector)
    else:
        raise Exception('Argument should not be empty list')
